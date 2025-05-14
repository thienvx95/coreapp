from typing import Generic, TypeVar, Type, Optional, List
from pydantic import BaseModel
from app.core.repository.base import BaseRepository
from app.core.logging import logger

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Base service class that provides common CRUD operations.
    """
    def __init__(self, repository: BaseRepository[ModelType, CreateSchemaType, UpdateSchemaType]):
        self.repository = repository
        self.logger = logger

    async def create(self, obj_in: CreateSchemaType) -> ModelType:
        """
        Create a new object.
        
        Args:
            obj_in: The data to create the object with
            
        Returns:
            The created object
        """
        try:
            return await self.repository.create(obj_in)
        except Exception as e:
            self.logger.error(f"Error in service create operation: {str(e)}")
            raise

    async def get(self, id: str) -> Optional[ModelType]:
        """
        Get an object by ID.
        
        Args:
            id: The object ID
            
        Returns:
            The object if found, None otherwise
        """
        try:
            return await self.repository.get(id)
        except Exception as e:
            self.logger.error(f"Error in service get operation: {str(e)}")
            raise

    async def list(
        self,
        skip: int = 0,
        limit: int = 10,
        filter_dict: dict = None
    ) -> List[ModelType]:
        """
        List objects with pagination and filtering.
        
        Args:
            skip: Number of objects to skip
            limit: Maximum number of objects to return
            filter_dict: Dictionary of filters to apply
            
        Returns:
            List of objects
        """
        try:
            return await self.repository.list(skip=skip, limit=limit, filter_dict=filter_dict)
        except Exception as e:
            self.logger.error(f"Error in service list operation: {str(e)}")
            raise

    async def update(
        self,
        id: str,
        obj_in: UpdateSchemaType
    ) -> Optional[ModelType]:
        """
        Update an object.
        
        Args:
            id: The object ID
            obj_in: The data to update the object with
            
        Returns:
            The updated object if found, None otherwise
        """
        try:
            return await self.repository.update(id, obj_in)
        except Exception as e:
            self.logger.error(f"Error in service update operation: {str(e)}")
            raise

    async def delete(self, id: str) -> bool:
        """
        Delete an object.
        
        Args:
            id: The object ID
            
        Returns:
            True if the object was deleted, False otherwise
        """
        try:
            return await self.repository.delete(id)
        except Exception as e:
            self.logger.error(f"Error in service delete operation: {str(e)}")
            raise

    async def count(self, filter_dict: dict = None) -> int:
        """
        Count objects with optional filtering.
        
        Args:
            filter_dict: Dictionary of filters to apply
            
        Returns:
            Number of objects
        """
        try:
            return await self.repository.count(filter_dict)
        except Exception as e:
            self.logger.error(f"Error in service count operation: {str(e)}")
            raise 