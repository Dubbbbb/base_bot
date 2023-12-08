from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage, RedisEventIsolation

from pydantic import SecretStr, HttpUrl, RedisDsn, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

import orjson
import ujson

from app.src.types.custom import ListStrEnv
from app.src.middlewares.bot import L10N, L10NMiddleware

__all__ = [
    "bot",
    "dp",
    "settings",
    "l10n_middleware",
]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        frozen=True
    )
    # general
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    ASSETS_DIR: Path = BASE_DIR / "assets"

    # application
    DOMAIN: HttpUrl
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = False
    DATABASE_URL: PostgresDsn

    # telegram
    TELEGRAM_BOT_TOKEN: SecretStr
    TELEGRAM_SECRET_TOKEN: SecretStr
    FSM_STORAGE_URL: RedisDsn
    ALLOWED_UPDATES: ListStrEnv

    # locale (l10n)
    LOCALE_PATH: Path = BASE_DIR / "locales/{locale}"
    ALLOWED_LOCALES: ListStrEnv
    DEFAULT_LOCALE: str
    RESOURCE_IDS: ListStrEnv = ["translation.ftl"]


settings = Settings()

fsm_storage = RedisStorage.from_url(
    url=settings.FSM_STORAGE_URL.unicode_string(),
    json_loads=orjson.loads,
    json_dumps=orjson.dumps
)
fsm_events_isolation = RedisEventIsolation(redis=fsm_storage.redis)
dp = Dispatcher(
    storage=fsm_storage,
    events_isolation=fsm_events_isolation
)
bot = Bot(
    token=settings.TELEGRAM_BOT_TOKEN.get_secret_value(),
    parse_mode=ParseMode.HTML,
    session=AiohttpSession(
        json_loads=ujson.loads,
        json_dumps=ujson.dumps
    )
)
l10n = L10N(
    locales=settings.ALLOWED_LOCALES,
    default_locale=settings.DEFAULT_LOCALE,
    resource_ids=settings.RESOURCE_IDS,
    roots=str(settings.LOCALE_PATH)
)
l10n_middleware = L10NMiddleware(l10n=l10n)
