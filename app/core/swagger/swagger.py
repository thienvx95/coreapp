from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi import FastAPI
from app.core.config import settings

def custom_openapi(app: FastAPI):
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="""
        FastAPI application with MongoDB integration.
        
        ## Features
        * CRUD operations for items
        * MongoDB integration
        * Async operations
        * Logging
        * Environment configuration
        
        ## Authentication
        Currently, this API does not require authentication.
        
        ## Rate Limiting
        No rate limiting is implemented yet.
        """,
        routes=app.routes,
    )
    
    # Custom documentation
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    
    # Add security schemes if needed
    # openapi_schema["components"]["securitySchemes"] = {
    #     "bearerAuth": {
    #         "type": "http",
    #         "scheme": "bearer",
    #         "bearerFormat": "JWT",
    #     }
    # }
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

def custom_swagger_ui_html(app: FastAPI):
    return get_swagger_ui_html(
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        title=f"{settings.APP_NAME} - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css",
        swagger_ui_parameters={
            "defaultModelsExpandDepth": -1,
            "docExpansion": "none",
            "filter": True,
            "syntaxHighlight.theme": "monokai",
        }
    ) 