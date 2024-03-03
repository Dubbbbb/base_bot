from aiogram import Router
from . import start

__all__ = ["router"]


router = Router(name="root")
router.include_router(router=start.router)
