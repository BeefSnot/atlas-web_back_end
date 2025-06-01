#!/usr/bin/env python3
"""
Password encryption module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with salt

    Args:
        password: The password string to hash

    Returns:
        A salted, hashed password as a byte string
    """
    # Convert password to bytes (required by bcrypt)
    encoded = password.encode('utf-8')

    # Generate salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded, salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password against a hashed password

    Args:
        hashed_password: The hashed password stored in the database
        password: The password provided for verification

    Returns:
        True if the password matches the hash, False otherwise
    """
    # Check if the password matches the hash
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
