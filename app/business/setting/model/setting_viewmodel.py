from typing import List, Optional, Union
from pydantic import BaseModel

# Define a type for setting values
SettingValue = Union[bool, str, int, List[str], None]

class SettingSelectOptionCreate(BaseModel):
    """
    Setting select option creation request model.
    """
    value: str
    label: str

    class Config:
        json_schema_extra = {
            "example": {
                "value": "option1",
                "label": "Option 1"
            }
        }

class SettingSelectOptionUpdate(BaseModel):
    """
    Setting select option update request model.
    """
    value: Optional[str] = None
    label: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "value": "option1_updated",
                "label": "Option 1 Updated"
            }
        }

class SettingCreate(BaseModel):
    """
    Setting creation request model.
    """
    type: str
    public: bool = False
    group: Optional[str] = None
    section: Optional[str] = None
    name: str
    value: Optional[SettingValue] = None
    sorter: Optional[int] = None
    hidden: bool = False
    description: Optional[str] = None
    values: Optional[List[SettingSelectOptionCreate]] = None

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

class SettingUpdate(BaseModel):
    """
    Setting update request model.
    """
    type: Optional[str] = None
    public: Optional[bool] = None
    group: Optional[str] = None
    section: Optional[str] = None
    name: Optional[str] = None
    value: Optional[SettingValue] = None
    sorter: Optional[int] = None
    hidden: Optional[bool] = None
    description: Optional[str] = None
    values: Optional[List[SettingSelectOptionUpdate]] = None
    updated_by: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "value": "#2196f3",
                "description": "Updated primary theme color"
            }
        }
