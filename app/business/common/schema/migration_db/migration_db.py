from datetime import datetime
from sqlmodel import Field
from app.business.common.schema.base import SqlBaseModel

class MigrationDB(SqlBaseModel, table=True):
    __tablename__ = "migrationDbs"
    fileName: str = Field(nullable=False, max_length=20)
    applied_at: datetime = Field(nullable=False)
    db_provider: str = Field(nullable=False, max_length=20)