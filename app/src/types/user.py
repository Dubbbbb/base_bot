from datetime import datetime, UTC

from pydantic import EmailStr, Field, PositiveInt

from .base import ImmutableSchema
from .custom import ASCIIAlphaStr

__all__ = [
    "UserCreateForm",
    "UserDetail",
    "UserUpdateForm",
]


class UserCreateForm(ImmutableSchema):
    email: EmailStr = Field(default=...)
    first_name: ASCIIAlphaStr = Field(default=..., min_length=2, max_length=32)
    last_name: ASCIIAlphaStr = Field(default=..., min_length=2, max_length=32)


class UserDetail(ImmutableSchema):
    id: PositiveInt = Field(default=...)
    email: EmailStr = Field(default=...)
    first_name: ASCIIAlphaStr = Field(default=..., min_length=2, max_length=32)
    last_name: ASCIIAlphaStr = Field(default=..., min_length=2, max_length=32)
    date_register: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    is_active: bool = Field(default=False)


class UserUpdateForm(UserCreateForm):
    id: PositiveInt = Field(default=...)
    is_active: bool = Field(default=False)
