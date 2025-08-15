from app.business.menu.model.menu_viewmodel import MenuCreate, MenuUpdate
from app.business.common.services.base import BaseService
from app.business.menu.schema.menu import Menu
from typing import List


class MenuService(BaseService[Menu, MenuCreate, MenuUpdate]):
    """
    Service for menu operations.
    """
    model = Menu
    
    def __init__(self):
        super().__init__()
        self.permission_service = None

    async def get_by_path(self, path: str) -> Menu | None:
        """
        Get a menu item by path.

        Args:
            path: The menu item's path

        Returns:
            The menu item if found, None otherwise
        """
        return await self.repository.find_one({"path": path})

    async def get_by_parent_id(self, parent_id: str) -> List[Menu]:
        """
        Get all menu items with the specified parent ID.

        Args:
            parent_id: The parent menu item's ID

        Returns:
            List of menu items
        """
        return await self.repository.list(filter_dict={"parentId": parent_id})

    async def get_root_menus(self) -> List[Menu]:
        """
        Get all root menu items (items without a parent).

        Returns:
            List of root menu items
        """
        return await self.repository.list(filter_dict={"parentId": None})

    async def get_menus_by_role(self, role_id: str) -> List[Menu]:
        """
        Get all menu items accessible by a specific role.

        Args:
            role_id: The role ID

        Returns:
            List of menu items accessible by the role
        """
        if not self.permission_service:
            raise ValueError("Permission service not initialized")

        # Get all permissions for the role
        permissions = await self.permission_service.get_by_role(role_id)

        # Extract function IDs from permissions
        function_ids = [permission.function_id for permission in permissions if permission.is_active]

        if not function_ids:
            return []

        # Get all menus with the function IDs
        menus = []
        for function_id in function_ids:
            if menu := await self.get(function_id):
                menus.append(menu)

        return menus
