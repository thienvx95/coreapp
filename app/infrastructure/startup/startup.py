from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.data.db_factory import DBFactory
from app.core.config import settings
from app.core.data.repository_factory import RepositoryFactory
from app.core.services.factory import ServiceFactory
from app.core.logging import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for application startup and shutdown events.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    # Startup
    logger.info("=" * 50)
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    logger.info(f"Environment: {settings.APP_ENV}")
    logger.info(f"Debug mode: {settings.DEBUG}")
    logger.info(f"API URL: http://{settings.HOST}:{settings.PORT}{settings.API_V1_STR}")
    logger.info(f"Database: {settings.DATABASE_NAME}")
    logger.info("=" * 50)

    # Connect to data
    DBFactory.initialize()
    provider = DBFactory.get_provider()
    db = await provider.connect()
    RepositoryFactory.initialize(db)
    ServiceFactory.initialize(db)
    print("Connected to MongoDB and initialized repositories")

    yield

    # Shutdown
    print(f"Shutting down {settings.APP_NAME}")
    await provider.close()
    print("Closed MongoDB connection")

def setup_startup_events(app: FastAPI) -> None:
    """
    Configure startup events for the application.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    app.lifespan = lifespan 