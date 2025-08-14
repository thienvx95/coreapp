from app.business.auth.view_model import AuthToken
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from app.business.auth.services.auth_service import AuthService
from app.business.user.entities.user import User
from app.core.config import settings
from app.core.container import Container
from datetime import datetime, timedelta

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
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_service.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    token = AuthToken(access_token=access_token, token_type="bearer")
    return token 