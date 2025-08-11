from fastapi import FastAPI
from app.core.config import settings
from app.api.api_v1.api import api_router
from app.core.container import Container
from app.infrastructure.startup import lifespan
from app.infrastructure.middleware import setup_middleware

app = FastAPI(
    title=settings.APP_NAME,
    description="FastAPI application with MongoDB integration",
    version=settings.APP_VERSION,
    docs_url=None,  # Disable default docs
    redoc_url=None,  # Disable default redoc
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    debug=settings.DEBUG,
    lifespan=lifespan,
)

setup_middleware(app)
app.include_router(api_router, prefix=settings.API_V1_STR)