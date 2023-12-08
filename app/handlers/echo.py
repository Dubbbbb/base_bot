from aiogram import Router
from aiogram.types import Message

__all__ = ["router"]


router = Router(name="echo")


@router.message()
async def echo(message: Message):
    await message.answer(text=message.text)
