from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.business.account.service.role_service import RoleService
from app.core.container import Container
from app.business.account.schema.role import Role
from app.business.account.model.role_viewmodel import RoleCreate, RoleUpdate, RoleViewModel

router = APIRouter()

def get_role_service() -> RoleService:
    """
    Get the role service instance.
    """
    return Container.role_service()

@router.post("/", response_model=RoleViewModel, status_code=status.HTTP_201_CREATED)
async def create_role(
    role_in: RoleCreate,
    role_service: RoleService = Depends(get_role_service)
) -> Role:
    """
    Create a new role.
    """
    # Check if role with name exists
    if await role_service.get_by_name(role_in.name):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Role with this name already exists"
        )
    
    return await role_service.create(role_in)

@router.get("/", response_model=List[RoleViewModel])
async def list_roles(
    skip: int = 0,
    limit: int = 10,
    role_service: RoleService = Depends(get_role_service)
) -> List[Role]:
    """
    List roles with pagination.
    """
    return await role_service.list(skip=skip, limit=limit)

@router.get("/{role_id}", response_model=RoleViewModel)
async def get_role(
    role_id: str,
    role_service: RoleService = Depends(get_role_service)
) -> Role:
    """
    Get a role by ID.
    """
    if role := await role_service.get(role_id):
        return role
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Role not found"
    )

@router.put("/{role_id}", response_model=RoleViewModel)
async def update_role(
    role_id: str,
    role_in: RoleUpdate,
    role_service: RoleService = Depends(get_role_service)
) -> Role:
    """
    Update a role.
    """
    if role := await role_service.update(role_id, role_in):
        return role
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Role not found"
    )

@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_role(
    role_id: str,
    role_service: RoleService = Depends(get_role_service)
) -> None:
    """
    Delete a role.
    """
    if not await role_service.delete(role_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found"
        )