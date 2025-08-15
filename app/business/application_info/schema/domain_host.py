from sqlalchemy import Boolean, Column, Integer, String

from app.business.common.schema.base import BaseModel

class DomainHost(BaseModel):
    __tablename__ = "domainHost"
    name = Column(String(20), nullable=False)
    port = Column(Integer, nullable=False)
    language = Column(String(5), nullable=False)
    domain = Column(String(20), nullable=False)
    scheme = Column(String(10), nullable=False)
    primary = Column(Boolean, nullable=False)
