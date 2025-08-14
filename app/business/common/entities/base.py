from datetime import datetime, UTC
from typing import Any, Optional, Union
from pydantic.types import UUID4
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class BaseModel(DeclarativeBase):
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
        
    id: Mapped[Union[UUID4, str]] = mapped_column(primary_key=True)
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]
    created_by: Mapped[Optional[str]] 
    updated_by: Mapped[Optional[str]]

    class Config:
        json_encoders = {UUID4: str}
        populate_by_name = True
        arbitrary_types_allowed = True 
