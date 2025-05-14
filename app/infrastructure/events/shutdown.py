from fastapi import FastAPI
from app.db.mongodb import close_mongo_connection
from app.core.config import settings
from app.core.logging import logger

def setup_shutdown_events(app: FastAPI) -> None:
    """
    Configure shutdown events for the application.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    @app.on_event("shutdown")
    async def shutdown_db_client():
        logger.info(f"Shutting down {settings.APP_NAME}")
        await close_mongo_connection()
        logger.info("Closed MongoDB connection") 