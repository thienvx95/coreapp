import uuid
from sqlalchemy import UUID, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True        
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    created_by = Column(UUID(as_uuid=True), nullable=True)
    updated_by = Column(UUID(as_uuid=True), nullable=True)
    
    def __repr__(self):
        return f'<{self.__class__.__name__} {self.id}>'
    
    # Utility functions for audit tracking
    def set_audit_fields(obj, user_id=None):
        """Helper function to set audit fields"""
        if hasattr(obj, 'created_by') and obj.created_by is None:
            obj.created_by = user_id
        if hasattr(obj, 'updated_by'):
            obj.updated_by = user_id
