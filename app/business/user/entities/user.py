from datetime import datetime
from typing import ClassVar, List, Optional, Annotated
from pydantic import BaseModel, EmailStr, Field, StringConstraints, computed_field
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import hashlib
from app.business.common.entities.base import BaseModel

class User(BaseModel):
    """
    User model representing a system user.
    """
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(30))
    username: Annotated[str, StringConstraints(min_length=3, max_length=50)] = Field(..., description="User's username")
    password: str = Field(..., description="Hashed password")
    first_name: Annotated[str, StringConstraints(max_length=50)] = Field(..., description="User's first name")
    last_name: Annotated[str, StringConstraints(max_length=50)] = Field(..., description="User's last name")
    avatar: Optional[str] = Field(None, description="URL to user's avatar image")
    last_login: Optional[datetime] = Field(None, description="Last login timestamp")
    language: str = Field(default="en", description="User's preferred language")
    roles: List[str] = Field(default=["user"], description="List of user roles")
    last_ip_address: Optional[str] = Field(None, description="Last IP address used for login")
    password_changed_at: Optional[datetime] = Field(None, description="Last password change timestamp")
    is_active: bool = Field(default=True, description="Whether the user account is active")

    @computed_field
    @property
    def gravatar_url(self) -> str:
        """
        Generate Gravatar URL based on user's email.
        Returns a URL to the user's Gravatar image.
        """
        # Create MD5 hash of the email
        email_hash = hashlib.md5(self.email.lower().encode()).hexdigest()
        # Return the Gravatar URL
        return f"https://www.gravatar.com/avatar/{email_hash}?d=identicon&s=200"

    def __init__(self, **data):
        super().__init__(**data)
        # Set default avatar to Gravatar if not provided
        if not self.avatar:
            self.avatar = self.gravatar_url

    class Config:
        json_schema_extra = {
            "example": {
                "email": "john.doe@example.com",
                "username": "johndoe",
                "first_name": "John",
                "last_name": "Doe",
                "avatar": "https://www.gravatar.com/avatar/1234567890abcdef?d=identicon&s=200",
                "language": "en",
                "roles": ["user"],
                "is_active": True
            }
        } 
