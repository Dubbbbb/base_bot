from aiogram import Router
from aiogram.types import Message
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters.command import Command

from fluent.runtime import FluentLocalization  # noqa

from src.types.custom import Localization
from src.settings import settings

__all__ = ["router"]


router = Router(name="start")


@router.message(Command("start"))
async def start(message: Message, _: Localization):
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="НАЧАТЬ",
                    web_app=WebAppInfo(
                        url=settings.DOMAIN.unicode_string()
                    )
                )
            ]
        ]
    )
    await message.answer(
            text="Пройдите тест в WebApp",
            reply_markup=reply_markup
        )
