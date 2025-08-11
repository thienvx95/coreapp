from typing import List, Optional, Union
from pydantic import BaseModel, Field

class MenuCreate(BaseModel):
    """
    Menu creation request model.
    """
    access: Optional[Union[str, List[str]]] = None
    authority: List[str]
    children: Optional[List["MenuCreate"]] = None
    hideChildrenInMenu: Optional[bool] = None
    hideInMenu: Optional[bool] = None
    icon: Optional[str] = None
    component: Optional[str] = None
    name: Optional[str] = None
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
