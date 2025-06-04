#!/usr/bin/env python3
"""
Authentication module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a path requires authentication
        Returns True if path is not in excluded_paths
        """
        if path is None:
            return True
            
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
            
        path_slash = path if path.endswith('/') else path + '/'
        
        for excluded_path in excluded_paths:
            if path_slash == excluded_path:
                return False
                
        return True

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header from the request
        """
        if request is None:
            return None
            
        if 'Authorization' not in request.headers:
            return None
            
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user from the request
        Returns None for now
        """
        return None
