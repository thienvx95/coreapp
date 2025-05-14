from typing import Generic, TypeVar, Type, List
from pydantic import BaseModel
from app.core.logging import logger

ModelType = TypeVar("ModelType", bound=BaseModel)
ViewModelType = TypeVar("ViewModelType", bound=BaseModel)

class BaseViewModelMapper(Generic[ModelType, ViewModelType]):
    """
    Base class for mapping between domain models and view models.
    """
    def __init__(self, model_class: Type[ModelType], view_model_class: Type[ViewModelType]):
        self.model_class = model_class
        self.view_model_class = view_model_class
        self.logger = logger

    def to_view_model(self, model: ModelType) -> ViewModelType:
        """
        Convert a domain model to a view model.
        
        Args:
            model: The domain model to convert
            
        Returns:
            The converted view model
        """
        try:
            return self.view_model_class(**model.model_dump())
        except Exception as e:
            self.logger.error(f"Error converting model to view model: {str(e)}")
            raise

    def to_view_models(self, models: List[ModelType]) -> List[ViewModelType]:
        """
        Convert a list of domain models to view models.
        
        Args:
            models: List of domain models to convert
            
        Returns:
            List of converted view models
        """
        try:
            return [self.to_view_model(model) for model in models]
        except Exception as e:
            self.logger.error(f"Error converting models to view models: {str(e)}")
            raise

    def to_model(self, view_model: ViewModelType) -> ModelType:
        """
        Convert a view model to a domain model.
        
        Args:
            view_model: The view model to convert
            
        Returns:
            The converted domain model
        """
        try:
            return self.model_class(**view_model.model_dump())
        except Exception as e:
            self.logger.error(f"Error converting view model to model: {str(e)}")
            raise

    def to_models(self, view_models: List[ViewModelType]) -> List[ModelType]:
        """
        Convert a list of view models to domain models.
        
        Args:
            view_models: List of view models to convert
            
        Returns:
            List of converted domain models
        """
        try:
            return [self.to_model(view_model) for view_model in view_models]
        except Exception as e:
            self.logger.error(f"Error converting view models to models: {str(e)}")
            raise 