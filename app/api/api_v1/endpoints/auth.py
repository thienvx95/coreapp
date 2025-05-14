from fastapi import APIRouter, Depends, HTTPException, status
from app.core.viewmodels.auth.auth_viewmodel import LoginRequest
from app.core.services.auth.auth_service import AuthService
from app.core.services.factory import ServiceFactory
from app.models.user import User

router = APIRouter()

def get_auth_service() -> AuthService:
    """
    Get the auth service instance.
    """
    return ServiceFactory.get_service(AuthService)

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