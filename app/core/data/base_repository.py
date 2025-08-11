from abc import ABC, abstractmethod
from typing import List, Dict, Any, Generic

from app.core.data.model_type import ModelType, CreateSchemaType, UpdateSchemaType
from app.business.common.view_model.pagingation import PaginationRequest, PaginationResponse

class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType], ABC):

    @abstractmethod
    async def insert_many(self, data: List[CreateSchemaType]) -> List[ModelType]:
        pass

    @abstractmethod
    async def insert_one(self, data: CreateSchemaType) -> List[ModelType]:
        pass

    @abstractmethod
    async def insert_if_not_exist(self, filter_dict: Dict[str, Any], data: CreateSchemaType) -> List[ModelType]:
        pass

    @abstractmethod
    async def update_one(self, filter_dict: Dict[str, Any], data: UpdateSchemaType) -> bool:
        pass

    @abstractmethod
    async def update_many(self, filter_dict: Dict[str, Any], data: List[UpdateSchemaType]) -> bool:
        pass

    @abstractmethod
    async def bulk_write(self,data: List[ModelType]) -> bool:
        pass

    @abstractmethod
    async def delete_one(self, _id: str) -> bool:
        pass

    @abstractmethod
    async def delete_many(self, filter_dict: Dict[str, Any]) -> bool:
        pass

    @abstractmethod
    async def find_one(self, filter_dict: Dict[str, Any]) -> ModelType:
        pass

    @abstractmethod
    async def find_many(self, filter_dict: Dict[str, Any]) -> List[ModelType]:
        pass

    @abstractmethod
    async def find_by_id(self, _id: str) -> ModelType:
        pass

    @abstractmethod
    async def find_paging(self, request: PaginationRequest) -> PaginationResponse:
        pass