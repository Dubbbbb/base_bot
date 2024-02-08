from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.orm import sessionmaker, Session

__all__ = [
    "DBSessionMiddleware",
]


class DBSessionMiddleware(BaseMiddleware):

    def __init__(self, session_maker: sessionmaker) -> None:
        self.session_maker = session_maker

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        with self.session_maker() as session:  # type: Session
            data["db_session"] = session
            return await handler(event, data)
