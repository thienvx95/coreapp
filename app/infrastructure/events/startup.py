from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.mongodb import connect_to_mongo, close_mongo_connection
from app.core.config import settings
from app.core.repository.factory import RepositoryFactory

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for application startup and shutdown events.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    # Startup
    print("=" * 50)
    print(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    print(f"Environment: {settings.APP_ENV}")
    print(f"Debug mode: {settings.DEBUG}")
    print(f"API URL: http://{settings.HOST}:{settings.PORT}{settings.API_V1_STR}")
    print(f"Database: {settings.DATABASE_NAME}")
    print("=" * 50)

    # Connect to database
    db = await connect_to_mongo()
    RepositoryFactory.initialize(db)
    print("Connected to MongoDB and initialized repositories")

    yield

    # Shutdown
    print(f"Shutting down {settings.APP_NAME}")
    await close_mongo_connection()
    print("Closed MongoDB connection")

def setup_startup_events(app: FastAPI) -> None:
    """
    Configure startup events for the application.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    app.lifespan = lifespan 