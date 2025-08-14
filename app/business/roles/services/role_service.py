from app.business.common.services.base import BaseService
from app.business.account.schema.role import Role
from app.business.roles.view_model.role_viewmodel import RoleCreate, RoleUpdate


class RoleService(BaseService[Role, RoleCreate, RoleUpdate]):
    """
    Service for role operations.
    """
    async def get_by_name(self, name: str) -> Role | None:
        """
        Get a role by name.
        
        Args:
            name: The role's name
            
        Returns:
            The role if found, None otherwise
        """
        return await self.repository.find_one({"name": name})