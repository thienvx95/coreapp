from abc import ABC, abstractmethod
from typing import Any

class BaseDatabaseProvider(ABC):
    @abstractmethod
    def get_database(self) -> Any:
        pass

    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def close(self):
        pass

    @abstractmethod
    async def ping(self):
        pass

    @abstractmethod
    async def get_database_name(self) -> str:
        pass

    @abstractmethod
    async def get_database_version(self) -> str:
        pass