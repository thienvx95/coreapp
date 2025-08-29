from app.business.common.schema.base import BaseModel
from sqlmodel import Field

class Setting(BaseModel, table=True):
    """
    Setting model representing a system setting.
    """
    __tablename__ = "settings"
    key: str = Field(nullable=False, max_length=100)
    type: str = Field(nullable=False, max_length=20)
    group: str = Field(nullable=True, max_length=50)
    section: str = Field(nullable=True, max_length=50)
    name: str = Field(nullable=False, max_length=50)
    value: str = Field(nullable=True)
    sorter: int = Field(nullable=True)
    hidden: bool = Field(nullable=False, default=False)
    description: str = Field(nullable=True, max_length=100)
    values: str = Field(nullable=True)

    class Config:
        json_schema_extra = {
            "example": {
                "type": "string",
                "public": True,
                "group": "appearance",
                "section": "theme",
                "name": "primaryColor",
                "value": "#1890ff",
                "sorter": 1,
                "hidden": False,
                "description": "Primary theme color"
            }
        }
