from sqlalchemy import Boolean, Column, Integer, String
from app.business.common.schema.base import BaseModel

class Menu(BaseModel):
    """
    Menu model representing a navigation menu item in the system.
    """
    __tablename__ = "menus"
    access = Column(String(20), nullable=True)
    authority = Column(String(20), nullable=False)
    children = Column(String(20), nullable=True)
    hideChildrenInMenu = Column(Boolean, nullable=True)
    hideInMenu = Column(Boolean, nullable=True)
    icon = Column(String(20), nullable=True)
    component = Column(String(20), nullable=True)
    name = Column(String(20), nullable=True)
    path = Column(String(20), nullable=False)
    layout = Column(Boolean, nullable=False)
    redirect = Column(String(100), nullable=True)
    exact = Column(Boolean, nullable=True)
    sortOrder = Column(Integer, nullable=True)
    parentId = Column(String(20), nullable=True)
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
