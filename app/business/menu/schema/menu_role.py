import uuid
from sqlmodel import Field
from app.business.common.schema.base import BaseModel

class MenuRole(BaseModel, table=True):
    """
    MenuRole model representing a relationship between a menu and a role.
    """
    __tablename__ = "menuRoles"
    menu_id: uuid.UUID = Field(nullable=False, foreign_key="menus.id", primary_key=True)
    role_id: uuid.UUID = Field(nullable=False, foreign_key="roles.id", primary_key=True)

    class Config:
        json_schema_extra = {
            "example": {
                "menu_id": "1",
                "role_id": "1"
            }
        }