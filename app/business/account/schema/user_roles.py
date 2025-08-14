from sqlalchemy import Column, ForeignKey, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.business.account.schema.user import User
from app.business.common.entities.base import BaseModel

class UserRole(BaseModel):
    __tablename__ = 'userRoles'
    
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    role_id = Column(UUID(as_uuid=True), ForeignKey('roles.id'), nullable=False)

    # Relationships
    user = relationship('User', foreign_keys=[user_id])
    role = relationship('Role', foreign_keys=[role_id])

    def __repr__(self):
        return f'<UserRole user_id={self.user_id} role_id={self.role_id}>'