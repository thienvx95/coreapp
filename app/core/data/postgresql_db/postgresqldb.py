from sqlalchemy import create_engine
from app.core.config import Settings
from sqlalchemy.orm import sessionmaker
from app.core.data.base_db import BaseDatabaseProvider
from app.business.common.entities.base import BaseModel

class PostGresqlDB(BaseDatabaseProvider):
    
    def __init__(self):
        pass

    async def connect(self):
        self.get_database().connection()

    async def close(self):
        self.get_database().close()

    async def ping(self):
        self.get_database().connection().execute("SELECT 1")
    
    def __get_engine(self):
        if self.engine is None:
            self.engine = create_engine(f"{Settings.DATABASE_URL}/{Settings.DATABASE_NAME}")
        return self.engine
    
    def create_table(self):
        BaseModel.metadata.create_all(bind=self.__get_engine())

    def get_database(self):
        if self.SessionLocal is None:
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.get_engine())
        return self.SessionLocal()
    
    async def get_database_name(self) -> str:
        return Settings.DATABASE_NAME

    async def get_database_version(self) -> str:
        pass