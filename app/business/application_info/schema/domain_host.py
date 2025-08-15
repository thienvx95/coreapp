from sqlalchemy import Boolean, Column, Integer, String

from app.business.common.schema.base import BaseModel

class DomainHost(BaseModel):
    __tablename__ = "domainHost"
    name = Column(String, nullable=False)
    port = Column(Integer, nullable=False)
    language = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    scheme = Column(String, nullable=False)
    primary = Column(Boolean, nullable=False)
