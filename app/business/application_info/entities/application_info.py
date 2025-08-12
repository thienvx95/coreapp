from typing import ClassVar
from pydantic import Field

from app.business.common.entities.base import BaseModel

class ApplicationInfo(BaseModel):
    collection_name: ClassVar[str] = "application_info"
    app_version: str = Field(..., description="Application version of the application")
    database_provider: str = Field(..., description="Database provider")
    database_name: str = Field(..., description="Database name")
    database_version: str = Field(..., description="Database version")
    database_migration: str = Field(..., description="Database migration version")
    cache_provider: str = Field(..., description="Cache provider")
