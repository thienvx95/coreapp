from app.business.common.services.base import BaseService
from app.business.permission.entities.permission import Permission
from app.business.permission.view_model.permission_viewmodel import PermissionCreate, PermissionUpdate
from typing import List, Optional


class PermissionService(BaseService[Permission, PermissionCreate, PermissionUpdate]):
    """
    Service for permission operations.
    """
    async def get_by_function_and_role(self, function_id: str, role_id: str) -> Optional[Permission]:
        """
        Get a permission by function ID and role ID.
        
        Args:
            function_id: The function (menu item) ID
            role_id: The role ID
            
        Returns:
            The permission if found, None otherwise
        """
        return await self.repository.find_one({"function_id": function_id, "role_id": role_id})
    
    async def get_by_function(self, function_id: str) -> List[Permission]:
        """
        Get all permissions for a specific function (menu item).
        
        Args:
            function_id: The function (menu item) ID
            
        Returns:
            List of permissions
        """
        return await self.repository.list(filter_dict={"function_id": function_id})
    
    async def get_by_role(self, role_id: str) -> List[Permission]:
        """
        Get all permissions for a specific role.
        
        Args:
            role_id: The role ID
            
        Returns:
            List of permissions
        """
        return await self.repository.list(filter_dict={"role_id": role_id})