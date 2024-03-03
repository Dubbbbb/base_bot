import asyncio

from bot import handlers
from src.settings import bot, dp, settings
from src.middlewares.bot import L10N, L10NMiddleware, DBSessionMiddleware
from src.database import session_maker


async def main() -> None:
    dp.include_router(router=handlers.router)

    l10n = L10N(
        locales=settings.ALLOWED_LOCALES,
        default_locale=settings.DEFAULT_LOCALE,
        resource_ids=settings.RESOURCE_IDS,
        roots=str(settings.LOCALE_PATH)
    )
    l10n_middleware = L10NMiddleware(l10n=l10n)

    db_session_middleware = DBSessionMiddleware(session_maker=session_maker)
    dp.message.middleware(db_session_middleware)
    dp.callback_query.middleware(db_session_middleware)

    dp.message.middleware(l10n_middleware)
    dp.callback_query.middleware(l10n_middleware)

    print("Telegram Bot starting")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
