from fastapi import APIRouter
from api.handlers import hello

main_router = APIRouter()
main_router.include_router(hello.router)
