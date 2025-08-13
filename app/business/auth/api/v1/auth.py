from app.business.auth.view_model.auth_viewmodel import LoginRequest
from fastapi import APIRouter, Depends, HTTPException, status
from app.business.auth.services.auth_service import AuthService
from app.business.user.entities.user import User
from app.core.container import Container

router = APIRouter()

def get_auth_service() -> AuthService:
    """
    Get the auth service instance.
    """
    return Container.auth_service()

@router.post("/login", response_model=User)
async def login(
    login_data: LoginRequest,
    auth_service: AuthService = Depends(get_auth_service)
) -> User:
    """
    Authenticate a user and return the user data.
    """
    user = await auth_service.authenticate(login_data.username, login_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    return user 