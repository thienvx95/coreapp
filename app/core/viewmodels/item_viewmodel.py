from datetime import datetime
from pydantic import BaseModel, Field
from app.models.item import Item
from app.core.viewmodels.base import BaseViewModelMapper

class ItemViewModel(BaseModel):
    """
    View model for item data.
    """
    id: str = Field(..., description="The item's unique identifier")
    name: str = Field(..., description="The item's name")
    description: str = Field(..., description="The item's description")
    price: float = Field(..., description="The item's price")
    is_available: bool = Field(..., description="Whether the item is available")
    created_at: datetime = Field(..., description="When the item was created")
    updated_at: datetime = Field(..., description="When the item was last updated")

    class Config:
        from_attributes = True

class ItemViewModelMapper(BaseViewModelMapper[Item, ItemViewModel]):
    """
    Mapper for converting between Item and ItemViewModel.
    """
    def __init__(self):
        super().__init__(Item, ItemViewModel)

    def to_view_model(self, model: Item) -> ItemViewModel:
        """
        Convert an Item to an ItemViewModel.
        
        Args:
            model: The Item to convert
            
        Returns:
            The converted ItemViewModel
        """
        try:
            return ItemViewModel(
                id=str(model.id),
                name=model.name,
                description=model.description,
                price=model.price,
                is_available=model.is_available,
                created_at=model.created_at,
                updated_at=model.updated_at
            )
        except Exception as e:
            self.logger.error(f"Error converting Item to ItemViewModel: {str(e)}")
            raise 