from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.business.roles.services.role_service import RoleService
from app.business.user.services.user_service import UserService
from app.business.user.view_model.user_viewmodel import UserCreate, UserUpdate
from app.business.account.schema.user import User
from app.core.container import Container

router = APIRouter()

def get_user_service() -> UserService:
    """
    Get the user service instance.
    """
    return Container.user_service()

def get_role_service() -> RoleService:
    """
    Get the role service instance.
    """
    return Container.role_service()

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate,
    user_service: UserService = Depends(get_user_service)
) -> User:
    """
    Create a new user.
    """
    # Check if user with email exists
    if await user_service.get_by_email(user_in.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )

    # Check if user with username exists
    if await user_service.get_by_username(user_in.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exists"
        )

    return await user_service.create(user_in)

@router.get("/", response_model=List[User])
async def list_users(
    skip: int = 0,
    limit: int = 10,
    user_service: UserService = Depends(get_user_service)
) -> List[User]:
    """
    List users with pagination.
    """
    return await user_service.list(skip=skip, limit=limit)

@router.get("/{user_id}", response_model=User)
async def get_user(
    user_id: str,
    user_service: UserService = Depends(get_user_service)
) -> User:
    """
    Get a user by ID.
    """
    if user := await user_service.get(user_id):
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

@router.put("/{user_id}", response_model=User)
async def update_user(
    user_id: str,
    user_in: UserUpdate,
    user_service: UserService = Depends(get_user_service)
) -> User:
    """
    Update a user.
    """
    if user := await user_service.update(user_id, user_in):
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: str,
    user_service: UserService = Depends(get_user_service)
) -> None:
    """
    Delete a user.
    """
    if not await user_service.delete(user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

@router.get("/{user_id}/roles", response_model=List[str])
async def get_user_roles(
    user_id: str,
    user_service: UserService = Depends(get_user_service)
) -> List[str]:
    """
    Get all roles for a user.
    """
    if user := await user_service.get(user_id):
        return user.roles
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

@router.post("/{user_id}/roles/{role_name}", response_model=User)
async def add_role_to_user(
    user_id: str,
    role_name: str,
    user_service: UserService = Depends(get_user_service),
    role_service: RoleService = Depends(get_role_service)
) -> User:
    """
    Add a role to a user.
    """
    # Check if role exists
    role = await role_service.get_by_name(role_name)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found"
        )

    # Add role to user
    if user := await user_service.add_role(user_id, role_name):
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

@router.delete("/{user_id}/roles/{role_name}", response_model=User)
async def remove_role_from_user(
    user_id: str,
    role_name: str,
    user_service: UserService = Depends(get_user_service),
    role_service: RoleService = Depends(get_role_service)
) -> User:
    """
    Remove a role from a user.
    """
    # Check if role exists
    role = await role_service.get_by_name(role_name)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found"
        )

    # Remove role from user
    if user := await user_service.remove_role(user_id, role_name):
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )
