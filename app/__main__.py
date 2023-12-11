import contextlib

from fastapi import FastAPI
from fastapi.applications import AppType

from app import api, handlers
from app.src.settings import bot, dp, settings
from app.src.middlewares.bot import RepositoriesMiddleware, L10N, L10NMiddleware
from app.src.repositories import TGUserRepository
from app.src.database import session_maker


@contextlib.asynccontextmanager
async def lifespan(app: AppType):  # noqa
    # application startup
    app.include_router(router=api.router)

    # bot startup
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(
        url=settings.DOMAIN.unicode_string().removesuffix("/") + app.url_path_for("telegram_webhook"),
        secret_token=settings.TELEGRAM_SECRET_TOKEN.get_secret_value()
    )
    dp.include_router(router=handlers.router)

    l10n = L10N(
        locales=settings.ALLOWED_LOCALES,
        default_locale=settings.DEFAULT_LOCALE,
        resource_ids=settings.RESOURCE_IDS,
        roots=str(settings.LOCALE_PATH)
    )
    l10n_middleware = L10NMiddleware(l10n=l10n)
    repositories_middleware = RepositoriesMiddleware(
        repositories={
            "telegram_users_repository": TGUserRepository(session_maker=session_maker)
        }
    )
    dp.message.middleware(repositories_middleware)
    dp.callback_query.middleware(repositories_middleware)

    dp.message.middleware(l10n_middleware)
    dp.callback_query.middleware(l10n_middleware)

    yield

    # bot shutdown
    await bot.delete_webhook(drop_pending_updates=True)


app = FastAPI(
    debug=settings.DEBUG,
    lifespan=lifespan
)


if __name__ == '__main__':
    from uvicorn import run
    run(
        app=app,
        host=settings.HOST,
        port=settings.PORT,
        use_colors=True
    )
