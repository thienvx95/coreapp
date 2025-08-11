from typing import ClassVar, Optional, Annotated
from pydantic import Field, StringConstraints
from app.business.common.entities.base import MongoBaseModel

class Role(MongoBaseModel):
    """
    Role model representing a user role in the system.
    """
    collection_name: ClassVar[str] = "roles"
    name: Annotated[str, StringConstraints(min_length=2, max_length=50)] = Field(..., description="Role name")
    description: Optional[str] = Field(None, description="Role description")
    is_active: bool = Field(default=True, description="Whether the role is active")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "admin",
                "description": "Administrator role with full access",
                "is_active": True
            }
        }
