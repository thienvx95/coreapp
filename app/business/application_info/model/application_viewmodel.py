import datetime
from pydantic import BaseModel, Field

class ApplicationInfoViewModel(BaseModel):
    """
    Application info view model.
    """
    id: str = Field(..., description="The id of the application info")
    name: str = Field(..., description="The name of the application info")
    description: str = Field(..., description="The description of the application info")
    version: str = Field(..., description="The version of the application info")
    created_at: str = Field(..., description="The created at of the application info")