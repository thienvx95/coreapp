from typing import Optional
from pydantic import BaseModel, Field

class PermissionCreate(BaseModel):
    """
    Permission creation request model.
    """
    function_id: str
    role_id: str
    create: bool = False
    delete: bool = False
    change: bool = False
    read: bool = False
    administer: bool = False
    is_active: bool = True

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
    function_id: Optional[str] = None
    role_id: Optional[str] = None
    create: Optional[bool] = None
    delete: Optional[bool] = None
    change: Optional[bool] = None
    read: Optional[bool] = None
    administer: Optional[bool] = None
    is_active: Optional[bool] = None

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
