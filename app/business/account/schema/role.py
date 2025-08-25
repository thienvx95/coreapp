from app.business.account.schema.user_roles import UserRole
from app.business.common.schema.base import BaseModel
from sqlmodel import Field, Relationship
from typing import TYPE_CHECKING, Optional
from app.business.menu.schema.menu_role import MenuRole
from app.business.permission.schema.permission import Permission

if TYPE_CHECKING:
    from app.business.account.schema.user import User
    from app.business.menu.schema.menu import Menu

class Role(BaseModel, table=True):
    """
    Role model representing a user role in the system.
    """
    __tablename__ = "roles"
    name: str = Field(unique=True, nullable=False, index=True, max_length=80)
    description: str = Field(nullable=True, max_length=255)
    is_active: bool = Field(default=True, nullable=False)
    
    # Many-to-many relationship with User
    users: Optional[list["User"]] = Relationship(back_populates='roles', link_model=UserRole, sa_relationship_kwargs={"lazy": "selectin"})
    
    # Many-to-many relationship with Menu
    menus: Optional[list["Menu"]] = Relationship(back_populates='roles', link_model=MenuRole, sa_relationship_kwargs={"lazy": "selectin"})
    
    # One-to-many relationship with Permission
    permissions: Optional[list['Permission']] = Relationship(back_populates='role', cascade_delete=True, sa_relationship_kwargs={"lazy": "selectin"})
    
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "admin",
                "description": "Administrator role with full access",
                "is_active": True
            }
        }
