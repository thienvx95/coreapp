import uuid
from sqlalchemy import UUID, Column, String

from app.business.common.schema.base import Base

class ApplicationInfo(Base):
    __tablename__ = "applicationInfo"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    app_version = Column(String(10), nullable=False)
    database_provider = Column(String(20), nullable=False)
    database_name = Column(String(20), nullable=False)
    database_version = Column(String(100), nullable=False)
    database_migration = Column(String(20), nullable=True)
    cache_provider = Column(String(20), nullable=False)
