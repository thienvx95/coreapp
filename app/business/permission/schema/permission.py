from app.business.common.entities.base import BaseModel
from sqlalchemy import Column, String, ForeignKey, UUID
from sqlalchemy.orm import relationship

class Permission(BaseModel):
    """
    Permission model representing access rights to a menu item for a specific role.
    """ 
    __tablename__ = 'permissions'
    name = Column(String(80), nullable=False, index=True)
    resource = Column(String(80), nullable=False)  # e.g., 'user', 'post', 'admin'
    action = Column(String(50), nullable=False)    # e.g., 'create', 'read', 'update', 'delete'
    description = Column(String(255), nullable=True)
    role_id = Column(UUID(as_uuid=True), ForeignKey('roles.id'), nullable=False)
    
    # Many-to-one relationship with Role
    role = relationship('Role', back_populates='permissions')
    def __repr__(self):
        return f'<Permission {self.name}: {self.action} on {self.resource}>'

