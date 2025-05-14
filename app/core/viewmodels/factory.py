from typing import Dict, Type
from app.core.viewmodels.base import BaseViewModelMapper
from app.core.viewmodels.item_viewmodel import ItemViewModelMapper

class ViewModelFactory:
    """
    Factory class for creating and managing view model mapper instances.
    """
    _mappers: Dict[str, BaseViewModelMapper] = {}

    @classmethod
    def get_mapper(cls, mapper_class: Type[BaseViewModelMapper]) -> BaseViewModelMapper:
        """
        Get or create a view model mapper instance.
        
        Args:
            mapper_class: The mapper class to instantiate
            
        Returns:
            An instance of the requested mapper
        """
        mapper_name = mapper_class.__name__
        if mapper_name not in cls._mappers:
            if mapper_class == ItemViewModelMapper:
                cls._mappers[mapper_name] = mapper_class()
            else:
                raise ValueError(f"Unknown mapper class: {mapper_class}")
        
        return cls._mappers[mapper_name]

    @classmethod
    def get_item_mapper(cls) -> ItemViewModelMapper:
        """
        Get the item view model mapper instance.
        
        Returns:
            An instance of ItemViewModelMapper
        """
        return cls.get_mapper(ItemViewModelMapper) 