
import datetime
from typing import Optional
from pydantic import BaseModel

class RefreshTokenCreate(BaseModel):
    token: str
    valid_until: datetime.datetime
    isActive: bool = True

    class Config:
        json_schema_extra = {
            "example": {
                "token": "1234567890",
                "valid_until": "2025-01-01 00:00:00",
                "isActive": True
            }
        }

class RefreshTokenUpdate(BaseModel):
    valid_until: Optional[datetime.datetime] = None
    isActive: Optional[bool] = None

    class Config:
        json_schema_extra = {
            "example": {
                "valid_until": "2025-01-01 00:00:00",
                "isActive": True
            }
        }

# This is needed for the self-referencing type hint to work
RefreshTokenCreate.model_rebuild()
RefreshTokenUpdate.model_rebuild()
