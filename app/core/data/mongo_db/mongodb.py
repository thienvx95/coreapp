from typing import Any

from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase

from app.core.config import settings
from app.core.data.base_db import BaseDatabaseProvider

class MongoDB(BaseDatabaseProvider):
    db: AsyncMongoClient
    def __init__(self):
        self.db = AsyncMongoClient(settings.MONGODB_URL)
    def get_database(self) -> AsyncDatabase:
        return self.db.get_database(settings.DATABASE_NAME)

    async def connect(self):
        self.db = AsyncMongoClient(settings.MONGODB_URL)

    async def close(self):
        await self.db.close()

    async def ping(self):
        await self.db.command("ping")

    async def get_database_name(self) -> str:
        return settings.DATABASE_NAME

    async def get_database_version(self) -> str:
        server_info = await self.db.server_info()
        return server_info["version"]


