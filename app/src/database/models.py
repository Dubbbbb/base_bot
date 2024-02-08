from datetime import datetime, UTC
from typing import TYPE_CHECKING

from .base import Base

from sqlalchemy import Column, BIGINT, BOOLEAN, VARCHAR, TIMESTAMP, ForeignKey
from sqlalchemy.orm import synonym, relationship

__all__ = [
    # metadata
    "Base",
    # models
    "User",
    "UserRole",
]


class UserRole(Base):
    __tablename__ = "user_roles"

    name = Column(VARCHAR(length=32), primary_key=True)

    user = relationship(argument="User")


class User(Base):
    __tablename__ = "users"

    id = Column(
        BIGINT,
        primary_key=True,
        comment="User Telegram ID"
    )
    is_active = Column(
        BOOLEAN,
        default=False,
        server_default="false",
        nullable=False,
        comment="Is the User active?"
    )
    email = Column(
        VARCHAR(length=128),
        nullable=False,
        unique=True,
        comment="User Email",
    )
    first_name = Column(
        VARCHAR(length=32),
        nullable=False,
        comment="User first name"
    )
    last_name = Column(
        VARCHAR(length=32),
        nullable=False,
        comment="User last name"
    )
    date_register = Column(
        TIMESTAMP(timezone=True),
        default=lambda: datetime.now(tz=UTC),
        nullable=False,
        comment="Date of user registration"
    )
    role = Column(
        VARCHAR(length=32),
        ForeignKey(column="user_roles.name", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False
    )


    def __str__(self) -> str:
        return self.full_name

