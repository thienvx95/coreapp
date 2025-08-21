from typing import TYPE_CHECKING
import uuid
from app.business.common.schema.base import BaseModel
from sqlmodel import Field, Relationship

if TYPE_CHECKING:
    from app.business.account.schema.role import Role

class Permission(BaseModel, table=True):
    """
    Permission model representing access rights to a menu item for a specific role.
    """ 
    __tablename__ = 'permissions'
    name: str = Field(nullable=False, index=True, max_length=80)
    resource: str = Field(nullable=False, max_length=80)  # e.g., 'user', 'post', 'admin'
    action: str = Field(nullable=False, max_length=50)    # e.g., 'create', 'read', 'update', 'delete'
    description: str = Field(nullable=True, max_length=255)
    role_id: uuid.UUID = Field(nullable=False, foreign_key="roles.id")
    
    # Many-to-one relationship with Role
    role: 'Role' = Relationship(back_populates='permissions')
    def __repr__(self):
        return f'<Permission {self.name}: {self.action} on {self.resource}>'

