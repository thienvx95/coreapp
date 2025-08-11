from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.logging import logger

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            # Log the error
            logger.exception(f"Error processing request: {str(e)}")
            
            # Return error response
            return JSONResponse(
                status_code=500,
                content={
                    "error": "Internal Server Error",
                    "detail": str(e) if request.app.debug else "An unexpected error occurred"
                }
            )

def setup_error_handler_middleware(app: FastAPI) -> None:
    """
    Configure error handling middleware for the application.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    app.add_middleware(ErrorHandlerMiddleware) 