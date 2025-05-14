from typing import Optional, List, Dict, Any
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.repository.base import BaseRepository
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

class ItemRepository(BaseRepository[Item, ItemCreate, ItemUpdate]):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db, "items", Item)

    async def get_by_name(self, name: str) -> Optional[Item]:
        """
        Get an item by its name.
        
        Args:
            name: The item name
            
        Returns:
            The item if found, None otherwise
        """
        try:
            if item := await self.collection.find_one({"name": name}):
                return Item(**item)
            return None
        except Exception as e:
            self.logger.error(f"Error retrieving item by name: {str(e)}")
            raise

    async def list_available(
        self,
        skip: int = 0,
        limit: int = 10
    ) -> List[Item]:
        """
        List available items.
        
        Args:
            skip: Number of items to skip
            limit: Maximum number of items to return
            
        Returns:
            List of available items
        """
        return await self.list(
            skip=skip,
            limit=limit,
            filter_dict={"is_available": True}
        )

    async def search(
        self,
        query: str,
        skip: int = 0,
        limit: int = 10
    ) -> List[Item]:
        """
        Search items by name or description.
        
        Args:
            query: The search query
            skip: Number of items to skip
            limit: Maximum number of items to return
            
        Returns:
            List of matching items
        """
        try:
            filter_dict = {
                "$or": [
                    {"name": {"$regex": query, "$options": "i"}},
                    {"description": {"$regex": query, "$options": "i"}}
                ]
            }
            return await self.list(skip=skip, limit=limit, filter_dict=filter_dict)
        except Exception as e:
            self.logger.error(f"Error searching items: {str(e)}")
            raise 