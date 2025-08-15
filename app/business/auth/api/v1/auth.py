from app.business.auth.model import AuthToken
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from app.business.auth.services.auth_service import AuthService
from app.business.account.schema.user import User
from app.core.container import Container

router = APIRouter()

def get_auth_service() -> AuthService:
    """
    Get the auth service instance.
    """
    return Container.auth_service()

@router.post("/token", response_model=AuthToken)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm ,
    auth_service: AuthService = Depends(get_auth_service)
) -> User:
    """
    Authenticate a user and return the user data.
    """
    user = await auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    token = await auth_service.get_token_data(user)
    return token 
    