from fastapi import APIRouter, Depends

from app.core.data.base_db import BaseDatabaseProvider
from app.core.data.db_factory import DBFactory
from app.core.config import settings
from app.core.logging import logger

router = APIRouter()

def get_db_provider() -> BaseDatabaseProvider:
    return DBFactory.get_provider()

@router.get("/", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "environment": settings.APP_ENV
    }

@router.get("/db", tags=["Health"])
async def db_health_check(db_provider: BaseDatabaseProvider = Depends(get_db_provider)):
    """
    Health check endpoint to verify the data connection.
    """
    try:
        # Ping the data
        await db_provider.ping()
        return {
            "status": "healthy",
            "data": "connected",
            "database_name": settings.DATABASE_NAME
        }
    except Exception as e:
        logger.error(f"Database health check failed: {str(e)}")
        return {
            "status": "unhealthy",
            "data": "disconnected",
            "error": str(e)
        } 