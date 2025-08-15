from typing import List, Optional, Union
from pydantic import BaseModel, Field

class MenuViewModel(BaseModel):
    """
    Menu view model.
    """
    id: str = Field(..., description="The id of the menu")
    name: str = Field(..., description="The name of the menu")
    path: str = Field(..., description="The path of the menu")
    layout: bool = Field(..., description="Whether the menu is layout")
    icon: Optional[str] = Field(..., description="The icon of the menu")
    component: Optional[str] = Field(..., description="The component of the menu")
    isActive: bool = Field(..., description="Whether the menu is active")

class MenuCreate(BaseModel):
    """
    Menu creation request model.
    """
    id: str = Field(..., description="The id of the menu")
    name: str = Field(..., description="The name of the menu")
    path: str = Field(..., description="The path of the menu")
    layout: bool = Field(..., description="Whether the menu is layout")
    icon: Optional[str] = Field(..., description="The icon of the menu")
    component: Optional[str] = Field(..., description="The component of the menu")
    isActive: bool = Field(..., description="Whether the menu is active")
    path: str
    layout: bool
    redirect: Optional[str] = None
    exact: Optional[bool] = None
    sortOrder: Optional[int] = None
    parentId: Optional[str] = None
    isActive: bool = True

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

class MenuUpdate(BaseModel):
    """
    Menu update request model.
    """
    access: Optional[Union[str, List[str]]] = None
    authority: Optional[List[str]] = None
    children: Optional[List["MenuUpdate"]] = None
    hideChildrenInMenu: Optional[bool] = None
    hideInMenu: Optional[bool] = None
    icon: Optional[str] = None
    component: Optional[str] = None
    name: Optional[str] = None
    path: Optional[str] = None
    layout: Optional[bool] = None
    redirect: Optional[str] = None
    exact: Optional[bool] = None
    sortOrder: Optional[int] = None
    parentId: Optional[str] = None
    isActive: Optional[bool] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Updated Dashboard",
                "icon": "new-dashboard-icon",
                "sortOrder": 1,
                "isActive": True
            }
        }

# This is needed for the self-referencing type hint to work
MenuCreate.model_rebuild()
MenuUpdate.model_rebuild()
