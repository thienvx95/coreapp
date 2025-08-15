from typing import ClassVar
from pydantic import Field
from sqlalchemy import Column, String

from app.business.common.schema.base import BaseModel

class ApplicationInfo(BaseModel):
    __tablename__ = "application_info"
    app_version = Column(String, nullable=False)
    database_provider = Column(String, nullable=False)
    database_name = Column(String, nullable=False)
    database_version = Column(String, nullable=False)
    database_migration = Column(String, nullable=True)
    cache_provider = Column(String, nullable=False)
