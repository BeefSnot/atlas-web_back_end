#!/usr/bin/env python3
"""encrypt_password module.

Implements helper functions to hash passwords using bcrypt and to
validate plaintext passwords against stored hashes.
"""
from __future__ import annotations

import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password using bcrypt with a generated salt.

    Args:
        password: plaintext password as a string
    Returns:
        The salted, hashed password as bytes.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validate that a plaintext password matches a stored bcrypt hash.

    Args:
        hashed_password: bcrypt hash as bytes
        password: candidate plaintext password
    Returns:
        True if password matches the hash, else False.
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
