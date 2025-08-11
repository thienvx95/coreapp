from typing import ClassVar, Optional
from pydantic import Field
from app.business.common.entities.base import MongoBaseModel

class Permission(MongoBaseModel):
    """
    Permission model representing access rights to a menu item for a specific role.
    """
    collection_name: ClassVar[str] = "permissions"
    function_id: str = Field(..., description="ID of the menu item this permission applies to")
    role_id: str = Field(..., description="ID of the role this permission applies to")
    create: bool = Field(default=False, description="Whether the role can create items")
    delete: bool = Field(default=False, description="Whether the role can delete items")
    change: bool = Field(default=False, description="Whether the role can modify items")
    read: bool = Field(default=False, description="Whether the role can read items")
    administer: bool = Field(default=False, description="Whether the role has administrative rights")
    is_active: bool = Field(default=True, description="Whether the permission is active")

    class Config:
        json_schema_extra = {
            "example": {
                "function_id": "60d21b4967d0d8992e610c85",
                "role_id": "60d21b4967d0d8992e610c86",
                "create": True,
                "delete": True,
                "change": True,
                "read": True,
                "administer": False,
                "is_active": True
            }
        }
