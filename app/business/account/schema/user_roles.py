import uuid

from sqlmodel import Field
from app.business.common.schema.base import BaseModel
    
class UserRole(BaseModel, table=True):
    __tablename__ = 'userRoles'
    
    user_id: uuid.UUID = Field(nullable=False, foreign_key="users.id", primary_key=True)
    role_id: uuid.UUID = Field(nullable=False, foreign_key="roles.id", primary_key=True)

    def __repr__(self):
        return f'<UserRole user_id={self.user_id} role_id={self.role_id}>'