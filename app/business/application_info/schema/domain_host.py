from sqlmodel import Field
from app.business.common.schema.base import BaseModel

class DomainHost(BaseModel, table=True):
    __tablename__ = "domainHost"
    name: str = Field(nullable=False, max_length=20)
    port: int = Field(nullable=False)
    language: str = Field(nullable=False, max_length=5)
    domain: str = Field(nullable=False, max_length=20)
    scheme: str = Field(nullable=False, max_length=10)
    primary: bool = Field(nullable=False)
