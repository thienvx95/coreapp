

from datetime import datetime, UTC
from typing import Any, Dict, List, Type
from app.business.common.model.pagingation.pagination_request import PaginationRequest
from app.business.common.model.pagingation.pagination_response import PaginationResponse
from app.core.data.base_repository import BaseRepository
from app.core.data.model_type import CreateSchemaType, ModelType, UpdateSchemaType
from sqlalchemy.orm import Session
from app.core.logging import logger
class PostgreSqlRepository(BaseRepository):
    def __init__(self, db: Session, model: Type[ModelType]):
        self.db = db
        self.model = model

    async def insert_many(self, data: List[CreateSchemaType]) -> List[ModelType]:
        """
        Insert many data into the database.
        Args:
            data: List of data to insert.
        Returns:
            List of inserted data.
        """
        try:
            self.db.add_all(data)
            self.db.commit()
            refresh_data = [self.db.refresh(item) for item in data]
            return refresh_data
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error inserting many data for model {self.model.__name__}: {e}")
            raise e
        finally:
            self.db.close()

    async def insert_one(self, data: CreateSchemaType) -> List[ModelType]:
        """
        Insert one data into the database.
        Args:
            data: Data to insert.
        Returns:
            Inserted data.
        """
        try:
            self.db.add(data)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error inserting one data for model {self.model.__name__}: {e}")
            raise e
        finally:
            self.db.close()
        return data

    async def insert_if_not_exist(self, filter_dict: Dict[str, Any], data: CreateSchemaType) -> List[ModelType]:
        """
        Insert one data into the database if it does not exist.
        Args:
            filter_dict: Filter to check if data exists.
            data: Data to insert.
        Returns:
            Inserted data.
        """
        try:
            existing_data = self.db.query(self.model).filter_by(**filter_dict).first()
            if existing_data:
                return existing_data
            else:
                self.db.add(data)
                self.db.commit()
                self.db.refresh(data)
                return data
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error inserting if not exist data for model {self.model.__name__}: {e}")
            raise e
        finally:
            self.db.close()

    async def update_one(self, filter_dict: Dict[str, Any], data: UpdateSchemaType) -> bool:  
        """
        Update one data in the database.
        Args:
            filter_dict: Filter to update data.
            data: Data to update.
        Returns:
            True if updated, False otherwise.
        """
        try:
            existing_data = self.db.query(self.model).filter_by(**filter_dict).first()
            if existing_data:
                for key, value in data.model_dump().items():
                    setattr(existing_data, key, value)

                if(hasattr(existing_data, 'updated_at')):
                    existing_data.updated_at = datetime.now(UTC)
                self.db.commit()
                return True
            else:
                self.db.add(data)
                self.db.commit()
                self.db.refresh(data)
                return True
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error updating one data for model {self.model.__name__}: {e}")
            raise e
        finally:
            self.db.close()

    async def update_many(self, filter_dict: Dict[str, Any], data: List[UpdateSchemaType]) -> bool:
        """
        Update many data in the database.
        Args:
            filter_dict: Filter to update data.
            data: Data to update.
        Returns:
            True if updated, False otherwise.
        """
        try:
            existing_data = self.db.query(self.model).filter_by(**filter_dict).all()
            if existing_data:
                for item in existing_data:
                    for key, value in data.model_dump().items():
                        setattr(item, key, value)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error updating many data for model {self.model.__name__}: {e}")
            raise e
        finally:
            self.db.close()

    async def bulk_write(self, data: List[ModelType]) -> bool:
        """
        Bulk write data into the database.
        Args:
            data: List of data to write.
        Returns:
            True if written, False otherwise.
        """
        try:
            self.db.add_all(data)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error bulk write data for model {self.model.__name__}: {e}")
            raise e
        finally:
            self.db.close()

    async def delete_one(self, _id: str) -> bool:
        """
        Delete one data from the database.
        Args:
            _id: ID of the data to delete.
        Returns:
            True if deleted, False otherwise.
        """
        try:
            self.db.query(self.model).filter_by(id=_id).delete()
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error deleting one data for model {self.model.__name__}: {e}")
            raise e
        finally:
            self.db.close()

    async def delete_many(self, filter_dict: Dict[str, Any]) -> bool:
        """
        Delete many data from the database.
        Args:
            filter_dict: Filter to delete data.
        Returns:
            True if deleted, False otherwise.
        """
        try:
            return self.db.query(self.model).filter_by(**filter_dict).first()
        except Exception as e:
            logger.error(f"Error deleting many data for model {self.model.__name__}: {e}")
            raise e
        finally:
            self.db.close()

    async def find_one(self, filter_dict: Dict[str, Any]) -> ModelType:
        """
        Find one data from the database.
        Args:
            filter_dict: Filter to find data.
        Returns:
            Found data.
        """
        try:
            data = self.db.query(self.model).filter_by(**filter_dict).first()
            return data
        except Exception as e:
            logger.error(f"Error finding one data for model {self.model.__name__}: {e}")
            raise e
        finally:
            self.db.close()

    async def find_many(self, filter_dict: Dict[str, Any]) -> List[ModelType]:
        """
        Find many data from the database.
        Args:
            filter_dict: Filter to find data.
        Returns:
            List of found data.
        """
        try:
            return self.db.query(self.model).filter_by(**filter_dict).all()
        except Exception as e:
            logger.error(f"Error finding many data for model {self.model.__name__}: {e}")
            raise e
        finally:
            self.db.close()
    
    async def find_by_id(self, _id: str) -> ModelType:
        """
        Find one data from the database by id.
        Args:
            _id: ID of the data to find.
        Returns:
            Found data.
        """
        try:    
            return self.db.query(self.model).filter_by(id=_id).first()
        except Exception as e:
            logger.error(f"Error finding one data by id for model {self.model.__name__}: {e}")
            raise e
        finally:
            self.db.close()

    async def find_paging(self, request: PaginationRequest) -> PaginationResponse:
        """
        Find paging data from the database.
        Args:
            request: Pagination request.
        Returns:
            Pagination response.
        """
        try:
            return self.db.query(self.model).filter_by(**request.filter_dict).offset((request.page - 1) * request.limit).limit(request.limit).all()
        except Exception as e:
            logger.error(f"Error finding paging data for model {self.model.__name__}: {e}")
            raise e
        finally:
            self.db.close()


        
