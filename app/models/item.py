from pydantic import Field
from app.models.base import MongoBaseModel

class Item(MongoBaseModel):
    name: str = Field(...)
    description: str = Field(...)
    price: float = Field(...)
    is_available: bool = Field(default=True) 