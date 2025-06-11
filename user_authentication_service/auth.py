#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hash a password string using bcrypt
    
    Args:
        password (str): The password to hash
        
    Returns:
        bytes: The salted hash of the input password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    return hashed_password


def _generate_uuid() -> str:
    """
    Generate a new UUID
    
    Returns:
        str: String representation of a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialize Auth instance
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user
        
        Args:
            email (str): User's email
            password (str): User's password
            
        Returns:
            User: Newly created User object
            
        Raises:
            ValueError: If a user with the given email already exists
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login credentials
        
        Args:
            email (str): User's email
            password (str): User's password
            
        Returns:
            bool: True if credentials are valid, False otherwise
        """
        try:
            user = self._db.find_user_by(email=email)
            
            return bcrypt.checkpw(
                password.encode('utf-8'),
                user.hashed_password
            )
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Create a new session for a user
        
        Args:
            email (str): User's email
            
        Returns:
            str: Session ID if user exists, None otherwise
        """
        try:
            user = self._db.find_user_by(email=email)
            
            session_id = _generate_uuid()
            
            self._db.update_user(user.id, session_id=session_id)
            
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Find a user by session ID
        
        Args:
            session_id (str): Session ID to look up
            
        Returns:
            User: User object if found, None otherwise
        """
        if session_id is None:
            return None
        
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroy a user's session by setting session_id to None
        
        Args:
            user_id (int): ID of the user whose session to destroy
            
        Returns:
            None
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            pass
        
        return None

    def get_reset_password_token(self, email: str) -> str:
        """
        Generate a reset password token for a user
        
        Args:
            email (str): User's email
            
        Returns:
            str: Reset token
            
        Raises:
            ValueError: If no user with the given email exists
        """
        try:
            user = self._db.find_user_by(email=email)
            
            reset_token = _generate_uuid()
            
            self._db.update_user(user.id, reset_token=reset_token)
            
            return reset_token
        except NoResultFound:
            raise ValueError("User does not exist")

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update a user's password using a reset token
    
        Args:
            reset_token (str): Reset token to find the user
            password (str): New password to set
        
        Returns:
            None
        
        Raises:
            ValueError: If no user with the given reset token exists
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        
            hashed_password = _hash_password(password)
        
            self._db.update_user(
                user.id, 
                hashed_password=hashed_password,
                reset_token=None
            )
        
            return None
        except NoResultFound:
            raise ValueError("Invalid reset token")
