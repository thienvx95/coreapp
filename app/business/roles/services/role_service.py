from app.core.container import Container
from app.business.common.services.base import BaseService
from app.business.roles.entities.role import Role
from app.business.roles.view_model.role_viewmodel import RoleCreate, RoleUpdate

class RoleService(BaseService[Role, RoleCreate, RoleUpdate]):
    """
    Service for role operations.
    """
    def __init__(self):
        repository = Container.generic_repository(collection_name="roles", model=Role)
        super().__init__(repository)
        self.repository = repository

    async def get_by_name(self, name: str) -> Role | None:
        """
        Get a role by name.
        
        Args:
            name: The role's name
            
        Returns:
            The role if found, None otherwise
        """
        return await self.repository.find_one({"name": name})