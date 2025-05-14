from fastapi import FastAPI
from app.db.mongodb import connect_to_mongo
from app.core.config import settings
from app.core.logging import logger
from app.core.repository.factory import RepositoryFactory

def setup_startup_events(app: FastAPI) -> None:
    """
    Configure startup events for the application.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    @app.on_event("startup")
    async def startup_db_client():
        logger.info(f"Starting up {settings.APP_NAME}")
        db = await connect_to_mongo()
        RepositoryFactory.initialize(db)
        logger.info("Connected to MongoDB and initialized repositories") 