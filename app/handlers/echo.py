from aiogram import Router
from aiogram.types import Message

from fluent.runtime import FluentLocalization  # noqa

from app.src.types.custom import Localization

__all__ = ["router"]


router = Router(name="echo")


@router.message()
async def echo(message: Message, _: Localization):
    await message.answer(text=_("Hello"))
