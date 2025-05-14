from typing import Optional, List
from app.core.services.base import BaseService
from app.core.repository.item_repository import ItemRepository
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate
from app.core.viewmodels.item_viewmodel import ItemViewModel
from app.core.viewmodels.factory import ViewModelFactory

class ItemService(BaseService[Item, ItemCreate, ItemUpdate]):
    """
    Service for handling item-related operations.
    """
    def __init__(self, repository: ItemRepository):
        super().__init__(repository)
        self.repository = repository
        self.view_model_mapper = ViewModelFactory.get_item_mapper()

    async def create(self, obj_in: ItemCreate) -> ItemViewModel:
        """
        Create a new item.
        
        Args:
            obj_in: The data to create the item with
            
        Returns:
            The created item as a view model
        """
        try:
            item = await super().create(obj_in)
            return self.view_model_mapper.to_view_model(item)
        except Exception as e:
            self.logger.error(f"Error in service create operation: {str(e)}")
            raise

    async def get(self, id: str) -> Optional[ItemViewModel]:
        """
        Get an item by ID.
        
        Args:
            id: The item ID
            
        Returns:
            The item as a view model if found, None otherwise
        """
        try:
            if item := await super().get(id):
                return self.view_model_mapper.to_view_model(item)
            return None
        except Exception as e:
            self.logger.error(f"Error in service get operation: {str(e)}")
            raise

    async def list(
        self,
        skip: int = 0,
        limit: int = 10,
        filter_dict: dict = None
    ) -> List[ItemViewModel]:
        """
        List items with pagination and filtering.
        
        Args:
            skip: Number of items to skip
            limit: Maximum number of items to return
            filter_dict: Dictionary of filters to apply
            
        Returns:
            List of items as view models
        """
        try:
            items = await super().list(skip=skip, limit=limit, filter_dict=filter_dict)
            return self.view_model_mapper.to_view_models(items)
        except Exception as e:
            self.logger.error(f"Error in service list operation: {str(e)}")
            raise

    async def update(
        self,
        id: str,
        obj_in: ItemUpdate
    ) -> Optional[ItemViewModel]:
        """
        Update an item.
        
        Args:
            id: The item ID
            obj_in: The data to update the item with
            
        Returns:
            The updated item as a view model if found, None otherwise
        """
        try:
            if item := await super().update(id, obj_in):
                return self.view_model_mapper.to_view_model(item)
            return None
        except Exception as e:
            self.logger.error(f"Error in service update operation: {str(e)}")
            raise

    async def get_by_name(self, name: str) -> Optional[ItemViewModel]:
        """
        Get an item by its name.
        
        Args:
            name: The item name
            
        Returns:
            The item as a view model if found, None otherwise
        """
        try:
            if item := await self.repository.get_by_name(name):
                return self.view_model_mapper.to_view_model(item)
            return None
        except Exception as e:
            self.logger.error(f"Error in service get_by_name operation: {str(e)}")
            raise

    async def list_available(
        self,
        skip: int = 0,
        limit: int = 10
    ) -> List[ItemViewModel]:
        """
        List available items.
        
        Args:
            skip: Number of items to skip
            limit: Maximum number of items to return
            
        Returns:
            List of available items as view models
        """
        try:
            items = await self.repository.list_available(skip=skip, limit=limit)
            return self.view_model_mapper.to_view_models(items)
        except Exception as e:
            self.logger.error(f"Error in service list_available operation: {str(e)}")
            raise

    async def search(
        self,
        query: str,
        skip: int = 0,
        limit: int = 10
    ) -> List[ItemViewModel]:
        """
        Search items by name or description.
        
        Args:
            query: The search query
            skip: Number of items to skip
            limit: Maximum number of items to return
            
        Returns:
            List of matching items as view models
        """
        try:
            items = await self.repository.search(query, skip=skip, limit=limit)
            return self.view_model_mapper.to_view_models(items)
        except Exception as e:
            self.logger.error(f"Error in service search operation: {str(e)}")
            raise 