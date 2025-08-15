from sqlalchemy import Column, String

from app.business.common.schema.base import BaseModel

class ApplicationInfo(BaseModel):
    __tablename__ = "application_info"
    app_version = Column(String(10), nullable=False)
    database_provider = Column(String(20), nullable=False)
    database_name = Column(String(20), nullable=False)
    database_version = Column(String(20), nullable=False)
    database_migration = Column(String(20), nullable=True)
    cache_provider = Column(String(20), nullable=False)
