from typing import TypeVar, List
from pydantic import BaseModel
from app.core.data.model_type import ModelType

class PaginationResponse(BaseModel):
    total: int
    total_pages: int
    data: List[ModelType]
    has_previous: bool
    has_next: bool
