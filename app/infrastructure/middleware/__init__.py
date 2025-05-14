from fastapi import FastAPI
from app.infrastructure.middleware.cors import setup_cors_middleware
from app.infrastructure.middleware.logging import setup_logging_middleware
from app.infrastructure.middleware.error_handler import setup_error_handler_middleware
from app.infrastructure.middleware.swagger import setup_swagger_middleware

def setup_middleware(app: FastAPI) -> None:
    """
    Setup all middleware for the application.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    # Setup middleware in order of execution
    setup_error_handler_middleware(app)  # First to catch all errors
    setup_logging_middleware(app)        # Then to log requests
    setup_cors_middleware(app)           # Then to handle CORS
    setup_swagger_middleware(app)        # Finally to setup Swagger documentation 