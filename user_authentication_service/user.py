#!/usr/bin/env python3
"""User model module.

Defines the SQLAlchemy Base and the User model mapped to the 'users' table.
"""
from __future__ import annotations

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """SQLAlchemy User model for the users table.

    Attributes:
        id: Integer primary key.
        email: Non-nullable email string.
        hashed_password: Non-nullable hashed password string.
        session_id: Nullable session identifier string.
        reset_token: Nullable reset token string.
    """

    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str | None = Column(String(250), nullable=True)
    reset_token: str | None = Column(String(250), nullable=True)
