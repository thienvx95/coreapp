from typing import List, Union
from pydantic import Field
from sqlalchemy import JSON, Boolean, Column, Integer, String
from app.business.common.schema.base import BaseModel

class SettingSelectOption(BaseModel):
    """
    Setting select option model representing an option for select and multiSelect settings.
    """
    value: str = Field(..., description="Option value")
    label: str = Field(..., description="Option display label")

    class Config:
        json_schema_extra = {
            "example": {
                "value": "option1",
                "label": "Option 1"
            }
        }

# Define a type for setting values
SettingValue = Union[bool, str, int, List[str], None]

class Setting(BaseModel):
    """
    Setting model representing a system setting.
    """
    __tablename__ = "settings"
    type = Column(String, nullable=False)
    public = Column(Boolean, nullable=False)
    group = Column(String, nullable=True)
    section = Column(String, nullable=True)
    name = Column(String, nullable=False)
    value = Column(String, nullable=True)
    sorter = Column(Integer, nullable=True)
    hidden = Column(Boolean, nullable=False)
    description = Column(String, nullable=True)
    values = Column(JSON, nullable=True)

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
