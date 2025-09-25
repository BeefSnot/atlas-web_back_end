#!/usr/bin/env python3
"""BasicAuth module for Basic Authentication."""
from api.v1.auth.auth import Auth
from typing import TypeVar
import base64
from models.user import User

class BasicAuth(Auth):
    """BasicAuth class for handling Basic Authentication."""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Returns the Base64 part of the Authorization header for Basic Auth."""
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decodes the Base64 string and returns the decoded value as UTF-8 string."""
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """Returns user email and password from Base64 decoded value."""
        if decoded_base64_authorization_header is None or not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, pwd = decoded_base64_authorization_header.split(':', 1)
        return email, pwd

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Returns User instance based on email and password."""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        users = User.search({'email': user_email})
        if not users or len(users) == 0:
            return None
        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the User instance for a request using Basic Auth."""
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        b64 = self.extract_base64_authorization_header(auth_header)
        if b64 is None:
            return None
        decoded = self.decode_base64_authorization_header(b64)
        if decoded is None:
            return None
        email, pwd = self.extract_user_credentials(decoded)
        if email is None or pwd is None:
            return None
        return self.user_object_from_credentials(email, pwd)
