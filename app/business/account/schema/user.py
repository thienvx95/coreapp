from datetime import datetime
import hashlib

from typing import TYPE_CHECKING
from app.business.account.schema.user_roles import UserRole
from app.business.common.schema.base import BaseModel
from sqlmodel import Field, Relationship
from sqlalchemy.ext.hybrid import hybrid_property

if TYPE_CHECKING:
    from app.business.account.schema.role import Role

class User(BaseModel, table=True):
    """
    User model representing a system user.
    """
    __tablename__ = "users"
    email: str = Field(unique=True, nullable=False, index=True, max_length=120)
    username: str = Field(unique=True, nullable=False, index=True, max_length=80)
    password: str = Field(nullable=False, max_length=255)
    first_name: str = Field(nullable=True, max_length=50)
    last_name: str = Field(nullable=True, max_length=50)
    is_active: bool = Field(default=True, nullable=False)
    last_login: datetime = Field(nullable=True)
    avatar: str = Field(nullable=True, max_length=255)
    language: str = Field(nullable=False, max_length=5)
    password_changed_at: datetime = Field(nullable=True)
    last_ip_address: str = Field(nullable=False, max_length=50)
    
    # Many-to-many relationship with Role
    roles: list['Role'] = Relationship(back_populates='users', link_model=UserRole)
    
    @hybrid_property
    def avatar(self):
        """Get user avatar URL with fallback to Gravatar"""
        if self.avatar_url:
            return self.avatar_url
        return self.get_gravatar_url()
    
    def get_gravatar_url(self, size=200, default='identicon'):
        """Generate Gravatar URL based on user email"""
        if not self.email:
            return self.get_default_avatar_url()
        
        # Create MD5 hash of lowercase email
        email_hash = hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()
        return f"https://www.gravatar.com/avatar/{email_hash}?d={default}&s={size}"
    
    def get_default_avatar_url(self, size=200):
        """Generate default avatar URL using first letter of username"""
        if not self.username:
            return f"https://www.gravatar.com/avatar/default?d=identicon&s={size}"
        
        first_letter = self.username[0].upper()
        # Use a service that generates letter avatars, or return a placeholder
        # You can replace this with your preferred avatar service
        return f"https://ui-avatars.com/api/?name={first_letter}&size={size}&background=random"
    
    @property
    def display_name(self):
        """Get user's display name"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        return self.username
    
    @property
    def initials(self):
        """Get user's initials"""
        if self.first_name and self.last_name:
            return f"{self.first_name[0]}{self.last_name[0]}".upper()
        elif self.first_name:
            return self.first_name[0].upper()
        return self.username[0].upper() if self.username else "U"
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def has_role(self, role_name):
        """Check if user has a specific role"""
        return any(role.name == role_name for role in self.roles)
    
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
