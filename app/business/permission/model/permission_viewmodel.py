from typing import Optional
from pydantic import BaseModel, Field

class PermissionViewModel(BaseModel):
    """
    Permission view model.
    """
    function_id: str = Field(..., description="The function id")
    role_id: str = Field(..., description="The role id")
    create: bool = Field(..., description="Whether the user can create")
    delete: bool = Field(..., description="Whether the user can delete")
    change: bool = Field(..., description="Whether the user can change")
    read: bool = Field(..., description="Whether the user can read")
    administer: bool = Field(..., description="Whether the user can administer")
    is_active: bool = Field(..., description="Whether the permission is active")
class PermissionCreate(BaseModel):
    """
    Permission creation request model.
    """
    function_id: str = Field(..., description="The function id")
    role_id: str = Field(..., description="The role id")
    create: bool = Field(..., description="Whether the user can create")
    delete: bool = Field(..., description="Whether the user can delete")
    change: bool = Field(..., description="Whether the user can change")
    read: bool = Field(..., description="Whether the user can read")
    administer: bool = Field(..., description="Whether the user can administer")
    is_active: bool = Field(..., description="Whether the permission is active")

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

class PermissionUpdate(BaseModel):
    """
    Permission update request model.
    """
    function_id: Optional[str] = Field(..., description="The function id")
    role_id: Optional[str] = Field(..., description="The role id")
    create: Optional[bool] = Field(..., description="Whether the user can create")
    delete: Optional[bool] = Field(..., description="Whether the user can delete")
    change: Optional[bool] = Field(..., description="Whether the user can change")
    read: Optional[bool] = Field(..., description="Whether the user can read")
    administer: Optional[bool] = Field(..., description="Whether the user can administer")
    is_active: Optional[bool] = Field(..., description="Whether the permission is active")

    class Config:
        json_schema_extra = {
            "example": {
                "create": True,
                "delete": False,
                "change": True,
                "read": True,
                "administer": False,
                "is_active": True
            }
        }
