from datetime import datetime, timedelta, UTC
from typing import Optional
from app.business.user.entities import User
from app.business.user.services.user_service import UserService
from app.core.utils.password import hash_password, verify_password
from jose import JWTError, jwt
from app.core.config import settings
import uuid

class AuthService:
    """
    Service for authentication operations.
    """
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def authenticate_user(self, username: str, password: str) -> User | None:
        """
        Authenticate a user.
        
        Args:
            username: The user's username
            password: The user's password
            
        Returns:
            The user if authentication succeeds, None otherwise
        """
        user = await self.user_service.get_by_username(username)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(UTC) + expires_delta
        else:
            expire = datetime.now(UTC) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt
    
    def create_refresh_token(data: dict):
        to_encode = data.copy()
        expire = datetime.now(UTC) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        jti = str(uuid.uuid4())  # Unique token ID
        
        to_encode.update({
            "exp": expire,
            "type": "refresh",
            "jti": jti
        })
        
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        
        # Store refresh token info
        refresh_token_store[jti] = {
            "username": data["sub"],
            "expires_at": expire,
            "revoked": False
        }
        
        return encoded_jwt

    def get_password_hash(self, password: str) -> str:
        """
        Get a password hash.
        
        Args:
            password: The password to hash
            
        Returns:
            The hashed password
        """
        return hash_password(password) 