from typing import List, Optional, Union
from pydantic import BaseModel, Field

# Define a type for setting values
SettingValue = Union[bool, str, int, List[str], None]

class SettingViewModel(BaseModel):
    """
    Setting view model.
    """
    id: str = Field(..., description="The id of the setting")
    name: str = Field(..., description="The name of the setting")
    value: SettingValue = Field(..., description="The value of the setting")
    type: str = Field(..., description="The type of the setting")
    public: bool = Field(..., description="Whether the setting is public")
    group: Optional[str] = Field(..., description="The group of the setting")
    section: Optional[str] = Field(..., description="The section of the setting")
    sorter: Optional[int] = Field(..., description="The sorter of the setting")
    hidden: bool = Field(..., description="Whether the setting is hidden")
    description: Optional[str] = Field(..., description="The description of the setting")
    values: Optional[str] = Field(..., description="The values of the setting")

class SettingSelectOptionCreate(BaseModel):
    """
    Setting select option creation request model.
    """
    value: str = Field(..., description="The value of the setting select option")
    label: str = Field(..., description="The label of the setting select option")

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
    value: Optional[str] = Field(..., description="The value of the setting select option")
    label: Optional[str] = Field(..., description="The label of the setting select option")

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
    type: str = Field(..., description="The type of the setting")
    public: bool = Field(..., description="Whether the setting is public")
    group: Optional[str] = Field(..., description="The group of the setting")
    section: Optional[str] = Field(..., description="The section of the setting")
    name: str = Field(..., description="The name of the setting")
    value: Optional[SettingValue] = Field(..., description="The value of the setting")
    sorter: Optional[int] = Field(..., description="The sorter of the setting")
    hidden: bool = Field(..., description="Whether the setting is hidden")
    description: Optional[str] = Field(..., description="The description of the setting")
    values: Optional[List[SettingSelectOptionCreate]] = Field(..., description="The values of the setting")

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
    type: Optional[str] = Field(..., description="The type of the setting")
    public: Optional[bool] = Field(..., description="Whether the setting is public")
    group: Optional[str] = Field(..., description="The group of the setting")
    section: Optional[str] = Field(..., description="The section of the setting")
    name: Optional[str] = Field(..., description="The name of the setting")
    value: Optional[SettingValue] = Field(..., description="The value of the setting")
    sorter: Optional[int] = Field(..., description="The sorter of the setting")
    hidden: Optional[bool] = Field(..., description="Whether the setting is hidden")
    description: Optional[str] = Field(..., description="The description of the setting")
    values: Optional[List[SettingSelectOptionUpdate]] = Field(..., description="The values of the setting")
    updated_by: Optional[str] = Field(..., description="The updated by of the setting")

    class Config:
        json_schema_extra = {
            "example": {
                "value": "#2196f3",
                "description": "Updated primary theme color"
            }
        }
