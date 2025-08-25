from typing import Optional
from app.business.account.schema.role import Role
from app.business.common.schema.base import BaseModel
from sqlmodel import Field, Relationship

from app.business.menu.schema.menu_role import MenuRole

class Menu(BaseModel, table=True):
    """
    Menu model representing a navigation menu item in the system.
    """
    __tablename__ = "menus"
    key: str = Field(nullable=False, max_length=20)
    access: str = Field(nullable=True, max_length=20)
    authority: str = Field(nullable=False, max_length=20)
    children: str = Field(nullable=True, max_length=20)
    hideChildrenInMenu: bool = Field(nullable=True)
    hideInMenu: bool = Field(nullable=True)
    icon: str = Field(nullable=True, max_length=20)
    component: str = Field(nullable=True, max_length=20)
    name: str = Field(nullable=True, max_length=20)
    path: str = Field(nullable=False, max_length=20)
    layout: bool = Field(nullable=False)
    redirect: str = Field(nullable=True, max_length=100)
    exact: bool = Field(nullable=True)
    sortOrder: int = Field(nullable=True)
    parentId: str = Field(nullable=True, max_length=20)
    isActive: bool = Field(nullable=False)
    
    roles: Optional[list["Role"]] = Relationship(back_populates='menus', link_model=MenuRole, sa_relationship_kwargs={"lazy": "selectin"})

    class Config:
        json_schema_extra = {
            "example": {
                "authority": ["admin"],
                "name": "Dashboard",
                "path": "/dashboard",
                "layout": False,
                "icon": "dashboard",
                "component": "Dashboard",
                "isActive": True
            }
        }
