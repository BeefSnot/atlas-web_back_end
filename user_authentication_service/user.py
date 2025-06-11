#!/usr/bin/env python3
"""
User model for the database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User class for representing users in the database
    
    Attributes:
        id (int): The primary key
        email (str): User's email (non-nullable)
        hashed_password (str): User's hashed password (non-nullable)
        session_id (str): User's session ID (nullable)
        reset_token (str): Password reset token (nullable)
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
