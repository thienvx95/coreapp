from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.business.application_info.services import ApplicationInfoService
from app.core.data import DBFactory
from app.core.config import settings
from app.core.logging import logger
from app.core.utils import get_banner
from app.core.container import Container

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for application startup and shutdown startup.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    # Startup
    get_banner()

    # Initialize Db
    await DBFactory().get_provider().connect()
    application_info_service: ApplicationInfoService = Container.application_info_service()
    await application_info_service.set_application_info()
    logger.info("Connected to MongoDB and initialized repositories")

    yield

    # Shutdown
    logger.info(f"Shutting down {settings.APP_NAME}")
    await DBFactory().get_provider().close()
    logger.info("Closed MongoDB connection")

def setup_startup_events(app: FastAPI) -> None:
    """
    Configure startup startup for the application.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    app.lifespan = lifespan 