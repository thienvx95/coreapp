from typing import Type, Optional, List, Dict, Any
from pymongo.asynchronous.database import AsyncDatabase
from pymongo.asynchronous.collection import AsyncCollection
from bson import ObjectId

from app.core.data.base_repository import BaseRepository
from app.core.data.model_type import ModelType, CreateSchemaType, UpdateSchemaType
from app.core.logging import logger
from app.business.common.view_model.pagingation import PaginationRequest, PaginationResponse


class MongoRepository(BaseRepository):
    db: AsyncDatabase
    model: Type[ModelType]
    def __init__(
        self,
        db: AsyncDatabase,
        model: Type[ModelType]
    ):
        self.db = db
        self.collection = getattr(model, "__tablename__", None)
        self.model = model


    async def insert_if_not_exist(self, filter_dict: Dict[str, Any], data: CreateSchemaType) -> List[ModelType]:
        pass

    async def update_one(self, filter_dict: Dict[str, Any], data: UpdateSchemaType) -> bool:
        """
        Update a document.

        Args:
            filter_dict: Dictionary of filters to apply
            data: The data to update the document with

        Returns:
            The updated document if found, None otherwise
        """
        try:
            obj_dict = data.model_dump(by_alias=True, exclude_unset=True)
            result = await self.collection.update_one(
                filter=filter_dict,
                update={"$set": obj_dict}
            )
            if result.modified_count == 0:
                logger.warning(f"Document not found for update in {self.collection.name} with filter: {filter_dict}")
                return None
            if updated_obj := await self.collection.find_one(filter=filter_dict):
                logger.info(f"Updated document in {self.collection.name} with filter: {filter_dict}")
                return self.model(**updated_obj)
            return None
        except Exception as e:
            logger.error(f"Error updating document in {self.collection.name}: {str(e)}")
            raise

    async def update_many(self, filter_dict: Dict[str, Any], data: List[UpdateSchemaType]) -> bool:
        pass

    async def bulk_write(self, data: List[ModelType]) -> bool:
        pass

    async def delete_one(self, _id: str) -> bool:
        """
        Delete a document.

        Args:
            _id The document ID

        Returns:
            True if the document was deleted, False otherwise
        """
        try:
            result = await self.collection.delete_one({"_id": ObjectId(_id)})
            if result.deleted_count == 0:
                logger.warning(f"Document not found for deletion in {self.collection.name} with id: {_id}")
                return False
            logger.info(f"Deleted document from {self.collection.name} with id: {_id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting document from {self.collection.name}: {str(e)}")
            raise

    async def delete_many(self, filter_dict: Dict[str, Any]) -> bool:
        pass

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
                logger.info(f"Found document in {self.collection.name} matching filter: {str(filter_dict)}")
                return self.model(**doc)
            logger.warning(f"No document found in {self.collection.name} matching filter: {str(filter_dict)}")
            return None
        except Exception as e:
            logger.error(f"Error finding document in {self.collection.name}: {str(e)}")
            raise

    async def find_many(self, filter_dict: Dict[str, Any]) -> List[ModelType]:
        pass

    async def find_by_id(self, _id: str) -> ModelType:
        """
        Get a document by its ID.

        Args:
            _id: The document ID

        Returns:
            The document if found, None otherwise
        """
        try:
            if obj := await self.collection.find_one({"_id": ObjectId(_id)}):
                logger.info(f"Retrieved document from {self.collection.name} with id: {_id}")
                return self.model(**obj)
            logger.warning(f"Document not found in {self.collection.name} with id: {_id}")
            return None
        except Exception as e:
            logger.error(f"Error retrieving document from {self.collection.name}: {str(e)}")
            raise

    async def find_paging(self, request: PaginationRequest) -> PaginationResponse:
        pass

    async def insert_one(self, data: CreateSchemaType) -> List[ModelType]:
        """
        Create a new document in the collection.

        Args:
            data: The data to create the document with

        Returns:
            The created document
        """
        try:
            obj_dict = data.model_dump(by_alias=True)
            result = await self.collection.insert_one(obj_dict)
            created_obj = await self.collection.find_one({"_id": result.inserted_id})
            logger.info(f"Created new document in {self.collection.name} with id: {result.inserted_id}")
            return self.model(**created_obj)
        except Exception as e:
            logger.error(f"Error creating document in {self.collection.name}: {str(e)}")
            raise

    async def insert_many(self, data: List[CreateSchemaType]):
        try:
            result = await self.collection.insert_many(data)
            logger.info(f"Created new documents in {self.collection.name} with id: {result.inserted_ids}")
        except Exception as e:
            logger.error(f"Error creating documents in {self.collection.name}: {str(e)}")
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