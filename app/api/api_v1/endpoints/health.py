from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.db.mongodb import get_database
from app.core.config import settings
from app.core.logging import logger

router = APIRouter()

@router.get("/", tags=["health"])
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "environment": settings.APP_ENV
    }

@router.get("/db", tags=["health"])
async def db_health_check(db: AsyncIOMotorDatabase = Depends(get_database)):
    """
    Health check endpoint to verify the database connection.
    """
    try:
        # Ping the database
        await db.command("ping")
        return {
            "status": "healthy",
            "database": "connected",
            "database_name": settings.DATABASE_NAME
        }
    except Exception as e:
        logger.error(f"Database health check failed: {str(e)}")
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        } 