from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models.item import Item
from app.db.mongodb import get_database
from app.services.item_service import ItemService
from app.core.logging import logger

router = APIRouter()

def get_item_service(db: AsyncIOMotorDatabase = Depends(get_database)) -> ItemService:
    return ItemService(db)

@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(
    item: Item,
    item_service: ItemService = Depends(get_item_service)
):
    try:
        return await item_service.create_item(item)
    except Exception as e:
        logger.error(f"Failed to create item: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create item"
        )

@router.get("/", response_model=List[Item])
async def read_items(
    skip: int = 0,
    limit: int = 10,
    item_service: ItemService = Depends(get_item_service)
):
    try:
        return await item_service.get_items(skip, limit)
    except Exception as e:
        logger.error(f"Failed to retrieve items: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve items"
        )

@router.get("/{item_id}", response_model=Item)
async def read_item(
    item_id: str,
    item_service: ItemService = Depends(get_item_service)
):
    try:
        if item := await item_service.get_item(item_id):
            return item
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to retrieve item {item_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve item"
        )

@router.put("/{item_id}", response_model=Item)
async def update_item(
    item_id: str,
    item: Item,
    item_service: ItemService = Depends(get_item_service)
):
    try:
        if updated_item := await item_service.update_item(item_id, item):
            return updated_item
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to update item {item_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update item"
        )

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(
    item_id: str,
    item_service: ItemService = Depends(get_item_service)
):
    try:
        if await item_service.delete_item(item_id):
            return
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to delete item {item_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete item"
        ) 