import uuid
from sqlmodel import Field 
from app.business.common.schema.base import SqlBaseModel

class ApplicationInfo(SqlBaseModel, table=True):
    __tablename__ = "applicationInfo"
    app_version: str = Field(nullable=False, max_length=10)
    database_provider: str = Field(nullable=False, max_length=20)
    database_name: str = Field(nullable=False, max_length=20)
    database_version: str = Field(nullable=False, max_length=100)
    database_migration: str = Field(nullable=True, max_length=20)
    cache_provider: str = Field(nullable=False, max_length=20)
