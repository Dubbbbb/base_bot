from typing import NoReturn

from fastapi import Depends, Header, HTTPException
from starlette.status import HTTP_403_FORBIDDEN

from src import settings

__all__ = [
    "TelegramSecretTokenExist",
]


async def telegram_secret_token_exist(x_telegram_bot_api_secret_token: str = Header()) -> NoReturn:
    """validate X-Telegram-Bot-Api-Secret-Token header

    :param x_telegram_bot_api_secret_token: header value
    :raise HTTPException: 403 if invalid header value
    """
    if x_telegram_bot_api_secret_token != settings.TELEGRAM_SECRET_TOKEN.get_secret_value():
        raise HTTPException(status_code=HTTP_403_FORBIDDEN)


TelegramSecretTokenExist = Depends(dependency=telegram_secret_token_exist)
