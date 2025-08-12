from typing import ClassVar
from pydantic import Field
from app.business.common.entities.base import BaseModel

class MigrationDB(BaseModel):
    collection_name: ClassVar[str] = "migration_dbs"
    fileName: str = Field(..., description="File name")
    applied_at: str = Field(..., description="Applied at")
    db_provider: str = Field(..., description="Database provider")