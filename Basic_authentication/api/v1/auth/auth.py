#!/usr/bin/env python3
<<<<<<< HEAD
"""Auth module for handling API authentication."""
from flask import request
from typing import List, TypeVar

class Auth:
    """Template for all authentication systems."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if authentication is required for a given path.

        Returns True if path is None, or excluded_paths is None or empty.
        Returns False if path is in excluded_paths (slash tolerant).
        """
        if path is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'
        for ex_path in excluded_paths:
            if ex_path.endswith('/') and path == ex_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the Authorization header from the request."""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user for the request."""
=======
"""Base authentication class for API v1."""

from typing import List, TypeVar
from flask import request


User = TypeVar('User')


class Auth:
    """Template class for authentication systems."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return True if path requires authentication.

        - True if path is None
        - True if excluded_paths is None or empty
        - False if path is in excluded_paths
        - Slash tolerant
        """
        if path is None:
            return True
        if not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Return the Authorization header value if present."""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """Return current user (not implemented)."""
>>>>>>> fb4997942433ff5d5191b7fd84256c4b7c006fa5
        return None
