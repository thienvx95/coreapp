from fastapi import FastAPI
from app.infrastructure.events.startup import setup_startup_events
from app.infrastructure.events.shutdown import setup_shutdown_events

def setup_events(app: FastAPI) -> None:
    """
    Setup all application lifecycle events.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    setup_startup_events(app)
    setup_shutdown_events(app) 