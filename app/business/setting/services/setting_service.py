from app.business.common.services.base import BaseService
from app.core.container import Container
from app.business.setting.entities.setting import Setting
from app.business.setting.view_model.setting_viewmodel import SettingCreate, SettingUpdate
from typing import List, Optional

class SettingService(BaseService[Setting, SettingCreate, SettingUpdate]):
    """
    Service for setting operations.
    """
    def __init__(self):
        repository = Container.generic_repository(collection_name="settings", model=Setting)
        super().__init__(repository)
        self.repository = repository

    async def get_by_name(self, name: str) -> Optional[Setting]:
        """
        Get a setting by name.
        
        Args:
            name: The setting's name
            
        Returns:
            The setting if found, None otherwise
        """
        return await self.repository.find_one({"name": name})
    
    async def get_by_group(self, group: str) -> List[Setting]:
        """
        Get all settings in a specific group.
        
        Args:
            group: The group name
            
        Returns:
            List of settings in the group
        """
        return await self.repository.list(filter_dict={"group": group})
    
    async def get_by_section(self, section: str) -> List[Setting]:
        """
        Get all settings in a specific section.
        
        Args:
            section: The section name
            
        Returns:
            List of settings in the section
        """
        return await self.repository.list(filter_dict={"section": section})
    
    async def get_by_group_and_section(self, group: str, section: str) -> List[Setting]:
        """
        Get all settings in a specific group and section.
        
        Args:
            group: The group name
            section: The section name
            
        Returns:
            List of settings in the group and section
        """
        return await self.repository.list(filter_dict={"group": group, "section": section})
    
    async def get_public_settings(self) -> List[Setting]:
        """
        Get all public settings.
        
        Returns:
            List of public settings
        """
        return await self.repository.list(filter_dict={"public": True})