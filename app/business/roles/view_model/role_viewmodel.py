from typing import Optional, Annotated
from pydantic import BaseModel, Field, StringConstraints

class RoleCreate(BaseModel):
    """
    Role creation request model.
    """
    name: Annotated[str, StringConstraints(min_length=2, max_length=50)]
    description: Optional[str] = None
    is_active: bool = True

    class Config:
        json_schema_extra = {
            "example": {
                "name": "admin",
                "description": "Administrator role with full access",
                "is_active": True
            }
        }

class RoleUpdate(BaseModel):
    """
    Role update request model.
    """
    name: Optional[Annotated[str, StringConstraints(min_length=2, max_length=50)]] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "editor",
                "description": "Editor role with limited access",
                "is_active": True
            }
        }
