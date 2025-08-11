from typing import ClassVar, List, Optional, Union
from pydantic import Field, HttpUrl
from app.business.common.entities.base import MongoBaseModel

class Menu(MongoBaseModel):
    """
    Menu model representing a navigation menu item in the system.
    """
    collection_name: ClassVar[str] = "menus"
    access: Optional[Union[str, List[str]]] = Field(None, description="Access control for the menu item")
    authority: List[str] = Field(..., description="Authority required to access this menu item")
    children: Optional[List["Menu"]] = Field(None, description="Child menu items")
    hideChildrenInMenu: Optional[bool] = Field(None, description="Whether to hide children in menu")
    hideInMenu: Optional[bool] = Field(None, description="Whether to hide this item in menu")
    icon: Optional[str] = Field(None, description="Icon for the menu item")
    component: Optional[str] = Field(None, description="Component to render for this menu item")
    name: Optional[str] = Field(None, description="Display name of the menu item")
    path: str = Field(..., description="URL path for the menu item")
    layout: bool = Field(..., description="Whether this item is a layout")
    redirect: Optional[str] = Field(None, description="Redirect URL if any")
    exact: Optional[bool] = Field(None, description="Whether path matching should be exact")
    sortOrder: Optional[int] = Field(None, description="Order for sorting menu items")
    parentId: Optional[str] = Field(None, description="ID of the parent menu item")
    isActive: bool = Field(default=True, description="Whether the menu item is active")

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

# This is needed for the self-referencing type hint to work
Menu.model_rebuild()
