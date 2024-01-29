from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import apps.settings as settings
from apps.views import api_router


def create_app():
    # https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI
    app = FastAPI()

    app.include_router(api_router, prefix=settings.API_PREFIX)

    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    return app
