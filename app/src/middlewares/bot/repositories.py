from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, CallbackQuery
from app.src.repositories.abstract import AbstractRepository

__all__ = [
    "RepositoriesMiddleware"
]


class RepositoriesMiddleware(BaseMiddleware):

    def __init__(self, repositories: dict[str, AbstractRepository]):
        self.repositories = repositories

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        for repository_name, repository in self.repositories.items():
            data[repository_name] = repository
        return await handler(event, data)
