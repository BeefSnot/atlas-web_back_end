#!/usr/bin/env python3
"""Password hashing and verification utilities using bcrypt."""

import bcrypt


def hash_password(password: str) -> bytes:
    """Return a salted, hashed password as bytes."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if provided password matches the hashed password."""
    return bcrypt.checkpw(password.encode(), hashed_password)
