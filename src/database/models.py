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
]


class User(Base):
    __tablename__ = "users"

    id = Column(
        BIGINT,
        primary_key=True,
        comment="User Telegram ID"
    )
    username = Column(
        VARCHAR(length=32),
        nullable=False,
        comment="User username"
    )
    email = Column(
        VARCHAR(length=128),
        nullable=False,
        unique=True,
        comment="User Email",
    )
    date_register = Column(
        TIMESTAMP(timezone=True),
        default=lambda: datetime.now(tz=UTC),
        nullable=False,
        comment="Date of user registration"
    )
    is_superuser = Column(
        BOOLEAN,
        nullable=False,
        default=False
    )


    def __str__(self) -> str:
        return self.full_name

