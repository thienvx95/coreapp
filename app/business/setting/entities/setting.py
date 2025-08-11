from typing import List, Optional, Union, Any
from pydantic import Field
from app.business.common.entities.base import MongoBaseModel

class SettingSelectOption(MongoBaseModel):
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

class Setting(MongoBaseModel):
    """
    Setting model representing a system setting.
    """
    type: str = Field(..., description="Setting type (boolean, string, int, select, multiSelect, font, date, group, section)")
    public: bool = Field(default=False, description="Whether the setting is public")
    group: Optional[str] = Field(None, description="Group the setting belongs to")
    section: Optional[str] = Field(None, description="Section within the group")
    name: str = Field(..., description="Setting name")
    value: Optional[SettingValue] = Field(None, description="Setting value")
    sorter: Optional[int] = Field(None, description="Order for sorting settings")
    hidden: bool = Field(default=False, description="Whether the setting is hidden")
    description: Optional[str] = Field(None, description="Setting description")
    values: Optional[List[SettingSelectOption]] = Field(None, description="Available options for select and multiSelect settings")

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
