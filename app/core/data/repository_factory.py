from typing import Type

from app.core.config import settings
from app.core.data.db_factory import DBFactory
from app.core.data.model_type import ModelType
from app.core.data.mongo_db.mongo_repository import MongoRepository
from app.core.data.postgresql_db.postgresql_repository import PostgreSqlRepository


class RepositoryFactory:
    def __init__(self):
        self._db_factory = DBFactory()

    def __get_repository_class(self):
        if settings.DB_PROVIDER.lower() == "mongodb":
            return MongoRepository
        elif settings.DB_PROVIDER.lower() == "postgresql":
            return PostgreSqlRepository
        else:
            raise ValueError(f"Invalid database provider: {settings.DB_PROVIDER}")
        
    def get_repository(self, model: Type[ModelType]):
        repository_cls = self.__get_repository_class()
        db = self._db_factory.get_provider().get_database()
        return repository_cls(db=db, model=model) 
    
