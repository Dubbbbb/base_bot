from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.cors import CORSMiddleware

from starlette.middleware.sessions import SessionMiddleware

from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from src import settings
from api.handlers import main_router


app = FastAPI(
    # docs_url=f"/api/docs",
    # redoc_url=f"/api/redoc",
    # openapi_url=f"/api/openapi.json"
)
# app.add_middleware(middleware_class=GZipMiddleware)
# app.add_middleware(
#     middleware_class=SessionMiddleware,
#     secret_key=settings.SESSION_SECRET_KEY.get_secret_value()
# )
# app.add_middleware(
#     middleware_class=ProxyHeadersMiddleware,
#     trusted_hosts="*",
# )
# app.add_middleware(
#     middleware_class=CORSMiddleware,
#     allow_origins=("*", ),
#     allow_methods=("GET", "POST", "PUT"),
#     allow_headers=("*", ),
#     allow_credentials=True,
# )

app.include_router(router=main_router)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app=app,
        host=settings.HOST,
        port=settings.PORT,
        use_colors=True
    )
