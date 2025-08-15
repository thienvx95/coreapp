from sqlalchemy import JSON, Boolean, Column, Integer, String
from app.business.common.schema.base import BaseModel

class Setting(BaseModel):
    """
    Setting model representing a system setting.
    """
    __tablename__ = "settings"
    type = Column(String(20), nullable=False)
    public = Column(Boolean, nullable=False)
    group = Column(String(20), nullable=True)
    section = Column(String(20), nullable=True)
    name = Column(String(20), nullable=False)
    value = Column(String(20), nullable=True)
    sorter = Column(Integer, nullable=True)
    hidden = Column(Boolean, nullable=False)
    description = Column(String(20), nullable=True)
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
