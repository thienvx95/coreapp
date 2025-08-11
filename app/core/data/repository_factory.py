from typing import Type

from app.core.config import settings
from app.core.data.db_factory import DBFactory
from app.core.data.model_type import ModelType
from app.core.data.mongo_db.mongo_repository import MongoRepository


class RepositoryFactory:
    def __init__(self):
        self._db_factory = DBFactory()

    def __get_repository_class(self):
        if settings.DB_PROVIDER.lower() == "mongodb":
            return MongoRepository
        
    def get_repository(self, model: Type[ModelType]):
        repository_cls = self.__get_repository_class()
        db = self._db_factory.get_provider().get_database()
        collection_name = getattr(model, "collection_name", None)
        return repository_cls(db=db, collection_name=collection_name, model=model) 
    
