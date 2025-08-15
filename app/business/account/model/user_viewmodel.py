from typing import List, Optional, Annotated
from pydantic import BaseModel, EmailStr, Field, StringConstraints

class UserViewModel(BaseModel):
    """
    User view model.
    """
    id: str = Field(..., description="The id of the user")
    email: EmailStr = Field(..., description="The email of the user")
    username: str = Field(..., description="The username of the user")
    first_name: str = Field(..., description="The first name of the user")
    last_name: str = Field(..., description="The last name of the user")
    language: str = Field(..., description="The language of the user")
    roles: List[str] = Field(..., description="The roles of the user")
    is_active: bool = Field(..., description="Whether the user is active")

class UserCreate(BaseModel):
    """
    User creation request model.
    """
    email: EmailStr
    username: Annotated[str, StringConstraints(min_length=3, max_length=50)]
    password: str
    first_name: Annotated[str, StringConstraints(max_length=50)]
    last_name: Annotated[str, StringConstraints(max_length=50)]
    language: str = "en"
    roles: List[str] = ["user"]
    is_active: bool = True

    class Config:
        json_schema_extra = {
            "example": {
                "email": "john.doe@example.com",
                "username": "johndoe",
                "password": "secretpassword",
                "first_name": "John",
                "last_name": "Doe",
                "language": "en",
                "roles": ["user"],
                "is_active": True
            }
        }

class UserUpdate(BaseModel):
    """
    User update request model.
    """
    email: Optional[EmailStr] = None
    username: Optional[Annotated[str, StringConstraints(min_length=3, max_length=50)]] = None
    password: Optional[str] = None
    first_name: Optional[Annotated[str, StringConstraints(max_length=50)]] = None
    last_name: Optional[Annotated[str, StringConstraints(max_length=50)]] = None
    avatar: Optional[str] = None
    language: Optional[str] = None
    roles: Optional[List[str]] = None
    is_active: Optional[bool] = None

    class Config:
        json_schema_extra = {
            "example": {
                "email": "john.doe@example.com",
                "username": "johndoe",
                "password": "newpassword",
                "first_name": "John",
                "last_name": "Doe",
                "avatar": "https://www.gravatar.com/avatar/1234567890abcdef",
                "language": "en",
                "roles": ["user", "admin"],
                "is_active": True
            }
        } 