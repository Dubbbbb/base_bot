from aiogram import Router
from aiogram.types import Message

from fluent.runtime import FluentLocalization  # noqa

__all__ = ["router"]


router = Router(name="echo")


@router.message()
async def echo(message: Message, _: FluentLocalization):
    await message.answer(text=message.text)
