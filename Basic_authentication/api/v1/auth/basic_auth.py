#!/usr/bin/env python3
"""
Basic authentication module for the API
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth"""
    
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 part from the Authorization header
        for Basic Authentication
        
        Args:
            authorization_header: The Authorization header string
            
        Returns:
            The Base64 encoded part of the header or None
        """
        if authorization_header is None:
            return None
            
        if not isinstance(authorization_header, str):
            return None
            
        if not authorization_header.startswith("Basic "):
            return None
            
        base64_part = authorization_header[6:]
        return base64_part
        
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64 string
        
        Args:
            base64_authorization_header: The Base64 string to decode
            
        Returns:
            The decoded value as a UTF-8 string or None
        """
        if base64_authorization_header is None:
            return None
            
        if not isinstance(base64_authorization_header, str):
            return None
            
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except Exception:
            return None
