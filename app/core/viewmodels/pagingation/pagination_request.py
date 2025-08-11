from typing import Optional, Dict, List
from pydantic import BaseModel

class PaginateRequest(BaseModel):
    limit: Optional[int] = 10
    page: Optional[int] = 1
    filter: Optional[Dict[str, List[str] | List[bool]]] = None
    search: Optional[Dict[str, str]] = None
    sort: Optional[Dict[str, str]] = None
    next: Optional[str] = None
    previous: Optional[str] = None