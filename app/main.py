from fastapi import FastAPI
from app.core.config import settings
from app.api.api_v1.api import api_router
from app.core.logging import logger
from app.infrastructure.middleware import setup_middleware
from app.infrastructure.events import setup_events

app = FastAPI(
    title=settings.APP_NAME,
    description="FastAPI application with MongoDB integration",
    version=settings.APP_VERSION,
    docs_url=None,  # Disable default docs
    redoc_url=None,  # Disable default redoc
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    debug=settings.DEBUG
)

# Setup all middleware
setup_middleware(app)

# Setup application events
setup_events(app)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/", tags=["root"])
async def root():
    """
    Root endpoint that returns basic API information.
    """
    return {
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.APP_ENV,
        "docs_url": "/docs",
        "api_url": f"{settings.API_V1_STR}"
    } 