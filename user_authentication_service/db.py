#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a user to the database

        Args:
            email (str): The user's email
            hashed_password (str): The user's hashed password

        Returns:
            User: The created user
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by arbitrary keyword arguments

        Args:
            **kwargs: Arbitrary keyword arguments to filter by

        Returns:
            User: The first matching user found

        Raises:
            NoResultFound: If no user is found
            InvalidRequestError: If invalid query arguments are provided
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
        except InvalidRequestError as e:
            raise e

        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update user attributes based on user_id

        Args:
            user_id (int): ID of the user to update
            **kwargs: Arbitrary keyword arguments with new attribute values

        Returns:
            None

        Raises:
            ValueError: If an invalid attribute is provided
        """
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"Can't update non-existent attribute: {key}")
            setattr(user, key, value)

        self._session.commit()
