from aiogram.types import Update
from fastapi import APIRouter, BackgroundTasks
from starlette.status import HTTP_200_OK

from app.src import bot, dp
from app.src.dependencies import TelegramSecretTokenExist

__all__ = ["router"]


router = APIRouter(
    prefix="/telegram",
    dependencies=(TelegramSecretTokenExist, )
)


@router.post(
    path="/webhook",
    status_code=HTTP_200_OK,
    name="telegram_webhook"
)
async def telegram_webhook(update: Update, background_tasks: BackgroundTasks):
    background_tasks.add_task(
        func=dp.feed_update,
        bot=bot,
        update=update
    )
    return {"status": "OK"}
