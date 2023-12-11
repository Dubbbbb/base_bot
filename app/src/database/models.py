from datetime import datetime, UTC
from typing import TYPE_CHECKING

from .base import Base

from sqlalchemy import Column, BIGINT, BOOLEAN, VARCHAR, TIMESTAMP, ForeignKey
from sqlalchemy.orm import synonym, relationship

__all__ = [
    # metadata
    "Base",
    # models
    "TGUser",
    "UserRole",
]


class UserRole(Base):
    __tablename__ = "user_roles"

    if TYPE_CHECKING:
        name: str
        users: list["TGUser"]
    else:
        name = Column(VARCHAR(length=32), primary_key=True)

        user = relationship(argument="TGUser")

    def __str__(self) -> str:
        return self.name

    def __len__(self) -> int:
        return len(self.user)

    def __getitem__(self, item) -> "TGUser":
        return self.users[item]


class TGUser(Base):
    __tablename__ = "telegram_users"

    if TYPE_CHECKING:
        id: int
        is_active: bool
        email: str
        first_name: str
        last_name: str
        date_register: datetime
        pk: int
        role: str
    else:
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

        pk = synonym("id")

    def __str__(self) -> str:
        return self.full_name

    def __bool__(self) -> bool:
        return self.is_active

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def total_working_days(self) -> int:
        return (datetime.now(tz=UTC) - self.date_register).days
