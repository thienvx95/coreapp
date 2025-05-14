from typing import Dict, Type
from app.core.services.base import BaseService
from app.core.repository.factory import RepositoryFactory
from app.core.services.user.user_service import UserService
from app.core.services.auth.auth_service import AuthService

class ServiceFactory:
    """
    Factory class for creating and managing service instances.
    """
    _services: Dict[str, BaseService] = {}

    @classmethod
    def initialize(cls) -> None:
        """
        Initialize all services.
        """

        # Initialize auth service
        auth_service = AuthService(None)  # Will be updated after user service is created
        cls._services[AuthService.__name__] = auth_service

        # Initialize user service
        user_service = UserService(user_repository, auth_service)
        cls._services[UserService.__name__] = user_service

        # Update auth service with user service
        auth_service.user_service = user_service

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
            raise ValueError(f"Unknown service class: {service_class}")
        
        return cls._services[service_name] 