from aiogram import Router
from aiogram.types import Message

from fluent.runtime import FluentLocalization  # noqa

from app.src.repositories import TGUserRepository
from app.src.types.custom import Localization

__all__ = ["router"]


router = Router(name="echo")


@router.message()
async def echo(message: Message, _: Localization, telegram_users_repository: TGUserRepository):
    print(telegram_users_repository)
    await message.answer(text=_("Hello"))
