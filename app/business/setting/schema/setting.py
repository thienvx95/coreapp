from app.business.common.schema.base import BaseModel
from sqlmodel import Field

class Setting(BaseModel, table=True):
    """
    Setting model representing a system setting.
    """
    __tablename__ = "settings"
    type: str = Field(nullable=False, max_length=20)
    public: bool = Field(nullable=False)
    group: str = Field(nullable=True, max_length=20)
    section: str = Field(nullable=True, max_length=20)
    name: str = Field(nullable=False, max_length=20)
    value: str = Field(nullable=True, max_length=20)
    sorter: int = Field(nullable=True)
    hidden: bool = Field(nullable=False)
    description: str = Field(nullable=True, max_length=20)
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
