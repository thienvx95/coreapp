from typing import Dict

from app.core.config import settings
from app.core.data.base_db import BaseDatabaseProvider
from app.core.data.mongo_db.mongodb import MongoDB
from app.core.data.postgresql_db.postgresqldb import PostGresqlDB

class DBFactory:
    provider = None
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_provider(self) -> BaseDatabaseProvider:
        if self.provider is None:
            if settings.DB_PROVIDER.lower() == "mongodb":
                 self.provider = MongoDB()
            elif settings.DB_PROVIDER.lower() == "postgresql":
                self.provider = PostGresqlDB()
            else:
                raise NotImplementedError
        return self.provider