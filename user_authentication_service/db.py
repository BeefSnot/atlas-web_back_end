#!/usr/bin/env python3
"""DB module.

Provides the DB class to interact with the users database via SQLAlchemy.
"""
from __future__ import annotations

from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

try:
    from .user import Base, User
except Exception:  # pragma: no cover - fallback for direct script usage
    from user import Base, User  # type: ignore


class DB:
    """DB class for managing SQLAlchemy sessions and user records."""

    def __init__(self) -> None:
        """Initialize a new DB instance with a SQLite engine and fresh schema."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session: Session | None = None

    @property
    def _session(self) -> Session:
        """Memoized session object.

        This is a private property and should not be used outside of DB.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Create and persist a new user.

        Args:
            email: User email address.
            hashed_password: Hashed password string.

        Returns:
            The created User instance.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        self._session.refresh(user)
        return user

    def find_user_by(self, **kwargs: Any) -> User:
        """Find the first user matching provided filters.

        Raises NoResultFound if no user matches, InvalidRequestError for invalid fields.
        """
        if not kwargs:
            raise InvalidRequestError("No query parameters provided")

        # Validate provided fields exist on the model
        for key in kwargs.keys():
            if not hasattr(User, key):
                raise InvalidRequestError(f"Invalid field: {key}")

        query = self._session.query(User).filter_by(**kwargs)
        user = query.first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs: Any) -> None:
        """Update attributes on a user identified by user_id.

        Raises ValueError if an invalid attribute is provided.
        """
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if not hasattr(User, key):
                raise ValueError(f"Invalid attribute: {key}")
            setattr(user, key, value)

        self._session.commit()
