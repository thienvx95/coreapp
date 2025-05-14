from typing import Dict, Type
from app.core.services.base import BaseService
from app.core.services.item_service import ItemService
from app.core.repository.factory import RepositoryFactory

class ServiceFactory:
    """
    Factory class for creating and managing service instances.
    """
    _services: Dict[str, BaseService] = {}

    @classmethod
    def get_service(cls, service_class: Type[BaseService]) -> BaseService:
        """
        Get or create a service instance.
        
        Args:
            service_class: The service class to instantiate
            
        Returns:
            An instance of the requested service
        """
        service_name = service_class.__name__
        if service_name not in cls._services:
            if service_class == ItemService:
                repository = RepositoryFactory.get_item_repository()
                cls._services[service_name] = service_class(repository)
            else:
                raise ValueError(f"Unknown service class: {service_class}")
        
        return cls._services[service_name]

    @classmethod
    def get_item_service(cls) -> ItemService:
        """
        Get the item service instance.
        
        Returns:
            An instance of ItemService
        """
        return cls.get_service(ItemService) 