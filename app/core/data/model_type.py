from typing import TypeVar
from app.business.common.schema.base import SqlBaseModel


ModelType = TypeVar("ModelType", bound=SqlBaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SqlBaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SqlBaseModel)