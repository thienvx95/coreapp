from sqlmodel import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.sql import text
from app.core.config import settings
from sqlalchemy.orm import sessionmaker
from app.core.data.base_db import BaseDatabaseProvider
from app.business.common.schema.base import BaseModel

class PostGresqlDB(BaseDatabaseProvider):
    engine: Engine = None
    SessionLocal: sessionmaker = None

    def __init__(self):
        super().__init__()

    async def connect(self):
        self.get_database().connection()

    async def close(self):
        self.get_database().close()

    async def ping(self):
        self.get_database().connection().execute("SELECT 1")
    
    def __get_engine(self):
        if self.engine is None:
            self.engine = create_engine(f"{settings.DATABASE_URL}/{settings.DATABASE_NAME}")
        return self.engine
    
    def create_table(self):
        BaseModel.metadata.create_all(bind=self.__get_engine())

    def get_database(self):
        if self.SessionLocal is None:
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.__get_engine())
        return self.SessionLocal()
    
    async def get_database_name(self) -> str:
        return settings.DATABASE_NAME

    async def get_database_version(self) -> str:
        return self.get_database().execute(text("SELECT version()")).scalar()