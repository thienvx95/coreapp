from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.business.menu.schema import Menu
from app.business.menu.services.menu_service import MenuService
from app.business.menu.model import MenuCreate, MenuUpdate, MenuViewModel
from app.business.account.service.role_service import RoleService
from app.core.container import Container

router = APIRouter()

def get_menu_service() -> MenuService:
    """
    Get the menu service instance.
    """
    return Container.menu_service()

def get_role_service() -> RoleService:
    """
    Get the role service instance.
    """
    return Container.role_service()

@router.post("/", response_model=MenuViewModel, status_code=status.HTTP_201_CREATED)
async def create_menu(
    menu_in: MenuCreate,
    menu_service: MenuService = Depends(get_menu_service)
) -> Menu:
    """
    Create a new menu item.
    """
    # Check if menu with path exists
    if await menu_service.get_by_path(menu_in.path):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Menu item with this path already exists"
        )

    return await menu_service.create(menu_in)

@router.get("/", response_model=List[MenuViewModel])
async def list_menus(
    skip: int = 0,
    limit: int = 100,
    menu_service: MenuService = Depends(get_menu_service)
) -> List[MenuViewModel]:
    """
    List menu items with pagination.
    """
    return await menu_service.list(skip=skip, limit=limit)

@router.get("/root", response_model=List[MenuViewModel])
async def get_root_menus(
    menu_service: MenuService = Depends(get_menu_service)
) -> List[MenuViewModel]:
    """
    Get all root menu items (items without a parent).
    """
    return await menu_service.get_root_menus()

@router.get("/{menu_id}", response_model=MenuViewModel)
async def get_menu(
    menu_id: str,
    menu_service: MenuService = Depends(get_menu_service)
) -> Menu:
    """
    Get a menu item by ID.
    """
    if menu := await menu_service.get(menu_id):
        return menu
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Menu item not found"
    )

@router.get("/{menu_id}/children", response_model=List[MenuViewModel])
async def get_menu_children(
    menu_id: str,
    menu_service: MenuService = Depends(get_menu_service)
) -> List[MenuViewModel]:
    """
    Get all children of a menu item.
    """
    if not await menu_service.get(menu_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Menu item not found"
        )
    return await menu_service.get_by_parent_id(menu_id)

@router.put("/{menu_id}", response_model=MenuViewModel)
async def update_menu(
    menu_id: str,
    menu_in: MenuUpdate,
    menu_service: MenuService = Depends(get_menu_service)
) -> Menu:
    """
    Update a menu item.
    """
    if menu := await menu_service.update(menu_id, menu_in):
        return menu
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Menu item not found"
    )

@router.delete("/{menu_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_menu(
    menu_id: str,
    menu_service: MenuService = Depends(get_menu_service)
) -> None:
    """
    Delete a menu item.
    """
    if not await menu_service.delete(menu_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Menu item not found"
        )

@router.get("/role/{role_id}", response_model=List[MenuViewModel])
async def get_menus_by_role(
    role_id: str,
    menu_service: MenuService = Depends(get_menu_service),
    role_service: RoleService = Depends(get_role_service)
) -> List[MenuViewModel]:
    """
    Get all menu items accessible by a specific role.
    """
    # Check if role exists
    if not await role_service.get(role_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found"
        )

    return await menu_service.get_menus_by_role(role_id)
