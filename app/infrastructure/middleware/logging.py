import time
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.logging import logger

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Start timer
        start_time = time.time()
        
        # Process request
        response = await call_next(request)
        
        # Calculate processing time
        process_time = time.time() - start_time
        
        # Log request details
        logger.info(
            f"Method: {request.method} Path: {request.url.path} "
            f"Status: {response.status_code} Duration: {process_time:.2f}s"
        )
        
        return response

def setup_logging_middleware(app: FastAPI) -> None:
    """
    Configure logging middleware for the application.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    app.add_middleware(LoggingMiddleware) 