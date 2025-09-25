#!/usr/bin/env python3
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
        return None
