from app.business.account.schema.user import User
from app.business.account.schema.user_roles import UserRole
from app.business.common.schema.base import BaseModel
from sqlmodel import Field, Relationship
from typing import TYPE_CHECKING
from app.business.permission.schema.permission import Permission

if TYPE_CHECKING:
    from app.business.account.schema.user import User

class Role(BaseModel, table=True):
    """
    Role model representing a user role in the system.
    """
    __tablename__ = "roles"
    name: str = Field(unique=True, nullable=False, index=True, max_length=80)
    description: str = Field(nullable=True, max_length=255)
    is_active: bool = Field(default=True, nullable=False)
    
    # Many-to-many relationship with User
    users: list["User"] = Relationship(back_populates='roles', link_model=UserRole)
        # One-to-many relationship with Permission
    permissions: list['Permission'] = Relationship(back_populates='role', cascade_delete=True)
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "admin",
                "description": "Administrator role with full access",
                "is_active": True
            }
        }
