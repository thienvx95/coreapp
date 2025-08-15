from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.business.permission.services.permission_service import PermissionService
from app.business.menu.services.menu_service import MenuService
from app.business.permission.view_model.permission_viewmodel import PermissionCreate, PermissionUpdate
from app.business.account.service.role_service import RoleService
from app.core.container import Container
from app.business.permission.schema.permission import Permission

router = APIRouter()

def get_permission_service() -> PermissionService:
    """
    Get the permission service instance.
    """
    return Container.permission_service()

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

@router.post("/", response_model=Permission, status_code=status.HTTP_201_CREATED)
async def create_permission(
    permission_in: PermissionCreate,
    permission_service: PermissionService = Depends(get_permission_service),
    menu_service: MenuService = Depends(get_menu_service),
    role_service: RoleService = Depends(get_role_service)
) -> Permission:
    """
    Create a new permission.
    """
    # Check if function (menu item) exists
    if not await menu_service.get(permission_in.function_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Function (menu item) not found"
        )
    
    # Check if role exists
    if not await role_service.get(permission_in.role_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Role not found"
        )
    
    # Check if permission already exists
    if await permission_service.get_by_function_and_role(permission_in.function_id, permission_in.role_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Permission for this function and role already exists"
        )
    
    return await permission_service.create(permission_in)

@router.get("/", response_model=List[Permission])
async def list_permissions(
    skip: int = 0,
    limit: int = 10,
    permission_service: PermissionService = Depends(get_permission_service)
) -> List[Permission]:
    """
    List permissions with pagination.
    """
    return await permission_service.list(skip=skip, limit=limit)

@router.get("/function/{function_id}", response_model=List[Permission])
async def get_permissions_by_function(
    function_id: str,
    permission_service: PermissionService = Depends(get_permission_service),
    menu_service: MenuService = Depends(get_menu_service)
) -> List[Permission]:
    """
    Get all permissions for a specific function (menu item).
    """
    # Check if function (menu item) exists
    if not await menu_service.get(function_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Function (menu item) not found"
        )
    
    return await permission_service.get_by_function(function_id)

@router.get("/role/{role_id}", response_model=List[Permission])
async def get_permissions_by_role(
    role_id: str,
    permission_service: PermissionService = Depends(get_permission_service),
    role_service: RoleService = Depends(get_role_service)
) -> List[Permission]:
    """
    Get all permissions for a specific role.
    """
    # Check if role exists
    if not await role_service.get(role_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found"
        )
    
    return await permission_service.get_by_role(role_id)

@router.get("/{permission_id}", response_model=Permission)
async def get_permission(
    permission_id: str,
    permission_service: PermissionService = Depends(get_permission_service)
) -> Permission:
    """
    Get a permission by ID.
    """
    if permission := await permission_service.get(permission_id):
        return permission
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Permission not found"
    )

@router.put("/{permission_id}", response_model=Permission)
async def update_permission(
    permission_id: str,
    permission_in: PermissionUpdate,
    permission_service: PermissionService = Depends(get_permission_service),
    menu_service: MenuService = Depends(get_menu_service),
    role_service: RoleService = Depends(get_role_service)
) -> Permission:
    """
    Update a permission.
    """
    # Check if function (menu item) exists if provided
    if permission_in.function_id and not await menu_service.get(permission_in.function_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Function (menu item) not found"
        )
    
    # Check if role exists if provided
    if permission_in.role_id and not await role_service.get(permission_in.role_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Role not found"
        )
    
    if permission := await permission_service.update(permission_id, permission_in):
        return permission
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Permission not found"
    )

@router.delete("/{permission_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_permission(
    permission_id: str,
    permission_service: PermissionService = Depends(get_permission_service)
) -> None:
    """
    Delete a permission.
    """
    if not await permission_service.delete(permission_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Permission not found"
        )