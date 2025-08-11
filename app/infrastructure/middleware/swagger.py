from fastapi import FastAPI
from app.core.swagger.swagger import custom_openapi, custom_swagger_ui_html

def setup_swagger_middleware(app: FastAPI) -> None:
    """
    Configure Swagger documentation middleware for the application.
    
    Args:
        app (FastAPI): The FastAPI application instance
    """
    # Custom OpenAPI schema
    app.openapi = lambda: custom_openapi(app)

    # Custom Swagger UI
    @app.get("/swagger", include_in_schema=False)
    async def custom_swagger_ui_html_route():
        return custom_swagger_ui_html(app) 