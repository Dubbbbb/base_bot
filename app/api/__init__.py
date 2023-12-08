from fastapi import APIRouter

from app.api import telegram

__all__ = ["router"]


router = APIRouter(prefix="/api")
router.include_router(router=telegram.router)
