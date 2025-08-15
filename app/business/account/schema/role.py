from sqlalchemy import Boolean, Column, String
from app.business.common.schema.base import BaseModel
from sqlalchemy.orm import relationship

class Role(BaseModel):
    """
    Role model representing a user role in the system.
    """
    __tablename__ = "roles"
    name = Column(String(80), unique=True, nullable=False, index=True)
    description = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    
    # Many-to-many relationship with User
    users = relationship(
        'User',
        secondary="userRoles",
        back_populates='roles',
        lazy='select'
    )
        # One-to-many relationship with Permission
    permissions = relationship('Permission', back_populates='role', cascade='all, delete-orphan')
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "admin",
                "description": "Administrator role with full access",
                "is_active": True
            }
        }
