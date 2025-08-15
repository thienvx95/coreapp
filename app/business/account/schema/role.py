from typing import ClassVar, Optional, Annotated
from pydantic import Field, StringConstraints
from app.business.common.schema.base import BaseModel
from sqlalchemy.orm import relationship

class Role(BaseModel):
    """
    Role model representing a user role in the system.
    """
    collection_name: ClassVar[str] = "roles"
    name: Annotated[str, StringConstraints(min_length=2, max_length=50)] = Field(..., description="Role name")
    description: Optional[str] = Field(None, description="Role description")
    is_active: bool = Field(default=True, description="Whether the role is active")
    
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
