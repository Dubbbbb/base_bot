import contextlib

from fastapi import FastAPI
from fastapi.applications import AppType

from app import api, handlers
from app.src.settings import bot, dp, settings


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
