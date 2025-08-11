from pydantic import Field
from app.business.common.entities.base import MongoBaseModel

class MigrationDB(MongoBaseModel):
    fileName: str = Field(..., description="File name")
    applied_at: str = Field(..., description="Applied at")
    db_provider: str = Field(..., description="Database provider")