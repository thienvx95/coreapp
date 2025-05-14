from typing import Dict, Type
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.repository.base import BaseRepository
from app.core.repository.item_repository import ItemRepository

class RepositoryFactory:
    """
    Factory class for creating and managing repository instances.
    """
    _repositories: Dict[str, BaseRepository] = {}
    _db: AsyncIOMotorDatabase = None

    @classmethod
    def initialize(cls, db: AsyncIOMotorDatabase) -> None:
        """
        Initialize the repository factory with a database connection.
        
        Args:
            db: The MongoDB database connection
        """
        cls._db = db

    @classmethod
    def get_repository(cls, repository_class: Type[BaseRepository]) -> BaseRepository:
        """
        Get or create a repository instance.
        
        Args:
            repository_class: The repository class to instantiate
            
        Returns:
            An instance of the requested repository
            
        Raises:
            ValueError: If the factory is not initialized
        """
        if not cls._db:
            raise ValueError("RepositoryFactory not initialized. Call initialize() first.")

        repository_name = repository_class.__name__
        if repository_name not in cls._repositories:
            cls._repositories[repository_name] = repository_class(cls._db)
        
        return cls._repositories[repository_name]

    @classmethod
    def get_item_repository(cls) -> ItemRepository:
        """
        Get the item repository instance.
        
        Returns:
            An instance of ItemRepository
        """
        return cls.get_repository(ItemRepository) 