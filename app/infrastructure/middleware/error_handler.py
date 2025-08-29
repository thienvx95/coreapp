from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import traceback
import sys
from app.core.logging import logger

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            # Log the error with traceback information
            exc_type, exc_value, exc_traceback = sys.exc_info()
            tb_info = traceback.extract_tb(exc_traceback)
            filename, line, func, text = tb_info[-1]
            logger.error(f"Error processing request: {str(e)} in file {filename}, line {line}, in function {func}")
            
            # Return error response
            error_detail = str(e)
            if request.app.debug:
                error_detail = f"{str(e)} in file {filename}, line {line}, in function {func}"
                
            return JSONResponse(
                status_code=500,
                content={
                    "error": "Internal Server Error",
                    "detail": error_detail if request.app.debug else "An unexpected error occurred"
                }
            )

def setup_error_handler_middleware(app: FastAPI) -> None:
    """
    Configure error handling middleware for the application.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    app.add_middleware(ErrorHandlerMiddleware) 