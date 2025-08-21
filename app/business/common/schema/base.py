from datetime import datetime, UTC
import uuid
from sqlalchemy import DateTime, func, text
from sqlmodel import SQLModel, Field, UUID

class SqlBaseModel(SQLModel):
    __abstract__ = True
    id: uuid.UUID = Field(default=None, sa_type=UUID(as_uuid=True), sa_column_kwargs={"server_default": text("gen_random_uuid()"),}, primary_key=True, unique=True, nullable=False)
class BaseModel(SqlBaseModel):
    __abstract__ = True        
    created_at: datetime = Field(default=None, sa_type=DateTime(timezone=True), sa_column_kwargs={"server_default": func.now()})
    updated_at: datetime = Field(default=None, sa_type=DateTime(timezone=True), sa_column_kwargs={"onupdate": func.utcnow()}, nullable=True)
    created_by: uuid.UUID = Field(nullable=True)
    updated_by: uuid.UUID = Field(nullable=True)
    
    # Utility functions for audit tracking
    def set_audit_fields(obj, user_id=None):
        """Helper function to set audit fields"""
        if hasattr(obj, 'created_by') and obj.created_by is None:
            obj.created_by = user_id
        if hasattr(obj, 'updated_by'):
            obj.updated_by = user_id
        obj.updated_at = datetime.now(UTC)
