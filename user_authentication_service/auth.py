#!/usr/bin/env python3
"""Authentication service module.

Provides password hashing, user registration, session management, and
password reset utilities backed by the DB abstraction.
"""
from __future__ import annotations

from typing import Optional

import bcrypt

try:
    from .db import DB
    from .user import User
except Exception:
    from db import DB
    from user import User


def _hash_password(password: str) -> bytes:
    """Return a salted hash of the input password as bytes.

    Uses bcrypt.hashpw with a generated salt.
    """
    if password is None:
        raise TypeError("password must be a string")
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a new UUID string."""
    import uuid

    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user or raise ValueError if the email exists."""
        try:
            self._db.find_user_by(email=email)
        except Exception:
            hashed = _hash_password(password)
            return self._db.add_user(email=email, hashed_password=hashed.decode("utf-8"))
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """Validate credentials for a user via bcrypt.checkpw."""
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return False
        if not user.hashed_password:
            return False
        try:
            return bcrypt.checkpw(
                password.encode("utf-8"), user.hashed_password.encode("utf-8")
            )
        except Exception:
            return False

    def create_session(self, email: str) -> Optional[str]:
        """Create a new session for the user and return the session_id."""
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: Optional[str]) -> Optional[User]:
        """Return the user associated with a given session_id, else None."""
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy a user's session by setting session_id to None."""
        try:
            user = self._db.find_user_by(id=user_id)
        except Exception:
            return None
        self._db.update_user(user.id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """Generate and persist a reset token for the given user email."""
        try:
            user = self._db.find_user_by(email=email)
        except Exception as exc:
            raise ValueError("User not found") from exc
        token = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)
        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update a user's password using a valid reset token.

        Raises ValueError if the token is invalid.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except Exception as exc:
            raise ValueError("Invalid reset token") from exc
        hashed = _hash_password(password).decode("utf-8")
        self._db.update_user(user.id, hashed_password=hashed, reset_token=None)
        return None
