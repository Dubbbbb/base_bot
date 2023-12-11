from .alchemy import SQLAlchemyRepository
from ..database import TGUser
from ..types import UserDetail


__all__ = [
    "TGUserRepository",
]


class TGUserRepository(SQLAlchemyRepository):
    model = TGUser
    detail_schema = UserDetail
