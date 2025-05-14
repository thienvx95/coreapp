from typing import Generic, TypeVar, Type, Optional, List, Dict, Any
from motor.motor_asyncio import AsyncIOMotorDatabase
from pydantic import BaseModel
from bson import ObjectId
from app.core.logging import logger

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(
        self,
        db: AsyncIOMotorDatabase,
        collection_name: str,
        model: Type[ModelType]
    ):
        self.db = db
        self.collection = db[collection_name]
        self.model = model

    async def create(self, obj_in: CreateSchemaType) -> ModelType:
        """
        Create a new document in the collection.
        
        Args:
            obj_in: The data to create the document with
            
        Returns:
            The created document
        """
        try:
            obj_dict = obj_in.model_dump(by_alias=True)
            result = await self.collection.insert_one(obj_dict)
            created_obj = await self.collection.find_one({"_id": result.inserted_id})
            logger.info(f"Created new document in {self.collection.name} with id: {result.inserted_id}")
            return self.model(**created_obj)
        except Exception as e:
            logger.error(f"Error creating document in {self.collection.name}: {str(e)}")
            raise

    async def get(self, id: str) -> Optional[ModelType]:
        """
        Get a document by its ID.
        
        Args:
            id: The document ID
            
        Returns:
            The document if found, None otherwise
        """
        try:
            if obj := await self.collection.find_one({"_id": ObjectId(id)}):
                logger.info(f"Retrieved document from {self.collection.name} with id: {id}")
                return self.model(**obj)
            logger.warning(f"Document not found in {self.collection.name} with id: {id}")
            return None
        except Exception as e:
            logger.error(f"Error retrieving document from {self.collection.name}: {str(e)}")
            raise

    async def list(
        self,
        skip: int = 0,
        limit: int = 10,
        filter_dict: Dict[str, Any] = None
    ) -> List[ModelType]:
        """
        List documents with pagination and filtering.
        
        Args:
            skip: Number of documents to skip
            limit: Maximum number of documents to return
            filter_dict: Dictionary of filters to apply
            
        Returns:
            List of documents
        """
        try:
            filter_dict = filter_dict or {}
            cursor = self.collection.find(filter_dict).skip(skip).limit(limit)
            documents = await cursor.to_list(length=limit)
            logger.info(f"Retrieved {len(documents)} documents from {self.collection.name}")
            return [self.model(**doc) for doc in documents]
        except Exception as e:
            logger.error(f"Error listing documents from {self.collection.name}: {str(e)}")
            raise

    async def update(
        self,
        id: str,
        obj_in: UpdateSchemaType
    ) -> Optional[ModelType]:
        """
        Update a document.
        
        Args:
            id: The document ID
            obj_in: The data to update the document with
            
        Returns:
            The updated document if found, None otherwise
        """
        try:
            obj_dict = obj_in.model_dump(by_alias=True, exclude_unset=True)
            result = await self.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": obj_dict}
            )
            if result.modified_count == 0:
                logger.warning(f"Document not found for update in {self.collection.name} with id: {id}")
                return None
            if updated_obj := await self.collection.find_one({"_id": ObjectId(id)}):
                logger.info(f"Updated document in {self.collection.name} with id: {id}")
                return self.model(**updated_obj)
            return None
        except Exception as e:
            logger.error(f"Error updating document in {self.collection.name}: {str(e)}")
            raise

    async def delete(self, id: str) -> bool:
        """
        Delete a document.
        
        Args:
            id: The document ID
            
        Returns:
            True if the document was deleted, False otherwise
        """
        try:
            result = await self.collection.delete_one({"_id": ObjectId(id)})
            if result.deleted_count == 0:
                logger.warning(f"Document not found for deletion in {self.collection.name} with id: {id}")
                return False
            logger.info(f"Deleted document from {self.collection.name} with id: {id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting document from {self.collection.name}: {str(e)}")
            raise

    async def count(self, filter_dict: Dict[str, Any] = None) -> int:
        """
        Count documents with optional filtering.
        
        Args:
            filter_dict: Dictionary of filters to apply
            
        Returns:
            Number of documents
        """
        try:
            filter_dict = filter_dict or {}
            count = await self.collection.count_documents(filter_dict)
            logger.info(f"Counted {count} documents in {self.collection.name}")
            return count
        except Exception as e:
            logger.error(f"Error counting documents in {self.collection.name}: {str(e)}")
            raise

    async def find_one(self, filter_dict: Dict[str, Any]) -> Optional[ModelType]:
        """
        Find a single document matching the filter criteria.
        
        Args:
            filter_dict: Dictionary of filters to apply
            
        Returns:
            The document if found, None otherwise
        """
        try:
            if doc := await self.collection.find_one(filter_dict):
                logger.info(f"Found document in {self.collection.name} matching filter: {filter_dict}")
                return self.model(**doc)
            logger.warning(f"No document found in {self.collection.name} matching filter: {filter_dict}")
            return None
        except Exception as e:
            logger.error(f"Error finding document in {self.collection.name}: {str(e)}")
            raise 