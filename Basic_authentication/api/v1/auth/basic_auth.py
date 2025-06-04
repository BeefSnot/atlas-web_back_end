#!/usr/bin/env python3
"""
Basic authentication module for the API
"""
from api.v1.auth.auth import Auth


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