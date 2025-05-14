from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

def setup_cors_middleware(app: FastAPI) -> None:
    """
    Configure CORS middleware for the application.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
        allow_credentials=settings.CORS_CREDENTIALS,
        allow_methods=settings.CORS_METHODS,
        allow_headers=settings.CORS_HEADERS,
    ) 