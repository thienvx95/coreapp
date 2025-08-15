from sqlalchemy import Column, DateTime, String
from app.business.common.schema.base import BaseModel

class MigrationDB(BaseModel):
    __tablename__ = "migrationDbs"
    fileName = Column(String, nullable=False)
    applied_at = Column(DateTime, nullable=False)
    db_provider = Column(String, nullable=False)