from sqlalchemy import Boolean, Column, Integer, String
from app.business.common.entities.base import BaseModel

class Menu(BaseModel):
    """
    Menu model representing a navigation menu item in the system.
    """
    __tablename__ = "menus"
    access = Column(String, nullable=True)
    authority = Column(String, nullable=False)
    children = Column(String, nullable=True)
    hideChildrenInMenu = Column(Boolean, nullable=True)
    hideInMenu = Column(Boolean, nullable=True)
    icon = Column(String, nullable=True)
    component = Column(String, nullable=True)
    name = Column(String, nullable=True)
    path = Column(String, nullable=False)
    layout = Column(Boolean, nullable=False)
    redirect = Column(String, nullable=True)
    exact = Column(Boolean, nullable=True)
    sortOrder = Column(Integer, nullable=True)
    parentId = Column(String, nullable=True)
    isActive = Column(Boolean, nullable=False)

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
