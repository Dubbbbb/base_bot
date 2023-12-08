from aiogram import Router

from app.handlers import echo

__all__ = ["router"]


router = Router(name="root")
router.include_router(router=echo.router)
