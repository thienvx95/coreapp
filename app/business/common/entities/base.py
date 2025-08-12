from datetime import datetime, UTC
from typing import Any, Optional, Union
from pydantic import BaseModel, Field
from pydantic.types import UUID4
from uuid import uuid4

class BaseModel(BaseModel):
    def __init__(self, **data: Any):
        super().__init__(**data)
        # Only set created_at during initial creation if it's not provided
        if not self.created_at:
            self.created_at = datetime.now(UTC)
        # Always update the updated_at timestamp
        self.updated_at = datetime.now(UTC)
        
    def update(self, **data: Any):
        """Update model and set updated_at timestamp"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now(UTC)
        return self
        
    id: Optional[Union[UUID4, str]] = Field(alias="_id", default=uuid4())
    created_at: datetime = Field(None, description="Created at")
    updated_at: datetime = Field(None, description="Updated at")
    created_by: Optional[str] = Field(None, description="ID of user who created this record")
    updated_by: Optional[str] = Field(None, description="ID of user who last updated this record")

    class Config:
        json_encoders = {UUID4: str}
        populate_by_name = True
        arbitrary_types_allowed = True 
