import datetime
from typing import ClassVar, Optional, Annotated
from pydantic import Field, StringConstraints
from app.business.common.schema.base import BaseModel

class RefreshToken(BaseModel):
    """
    Refresh Token model for the system
    """
    collection_name: ClassVar[str] = "refresh"
    user_id: str = Field(..., description="User ID")
    token: str = Field(..., description="Refresh token", unique=True)
    valid_until: datetime = Field(..., description="Valid until")
    is_active: bool = Field(default=True, description="Whether the refresh token is active")

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "1234567890",
                "token": "1234567890",
                "valid_until": "2025-01-01 00:00:00",
                "is_active": True
            }
        }
