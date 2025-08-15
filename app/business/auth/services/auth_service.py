from datetime import datetime, timedelta, UTC
from typing import Optional
from app.business.account.schema import User
from app.business.account.service.user_service import UserService
from app.core.utils.password import hash_password, verify_password
from jose import JWTError, jwt
from app.core.config import settings
from app.business.auth.view_model import TokenData
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
    
    def __create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
        """
        Create an access token for the user.
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(UTC) + expires_delta
        else:
            expire = datetime.now(UTC) + timedelta(minutes=15)
        to_encode.update({"exp": expire, "type": "access"})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    def __create_refresh_token(self, data: dict) -> str:
        """
        Create a refresh token for the user.
        """
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
     
    def get_token_data(self, user: User) -> TokenData:
        """
        Get the token data for the user.
        """
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.__create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        refresh_token = self.__create_refresh_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return TokenData(token=access_token, token_type="bearer")

    async def store_refresh_token_mongo(
        user_id: str, 
        username: str, 
        refresh_token: str,
        device_info: Optional[str] = None,
        ip_address: Optional[str] = None
        ):
        """Store refresh token in separate MongoDB collection"""
        refresh_tokens_collection = get_refresh_tokens_collection()
        expire_date = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        
        token_doc = {
            "_id": str(uuid.uuid4()),
            "token": refresh_token,
            "user_id": user_id,
            "username": username,
            "device_info": device_info,
            "ip_address": ip_address,
            "expires_at": expire_date,
            "created_at": datetime.utcnow(),
            "last_used": None,
            "is_active": True
        }
        
        await refresh_tokens_collection.insert_one(token_doc)
        return token_doc["_id"]

    def get_password_hash(self, password: str) -> str:
        """
        Get a password hash.
        
        Args:
            password: The password to hash
            
        Returns:
            The hashed password
        """
        return hash_password(password) 