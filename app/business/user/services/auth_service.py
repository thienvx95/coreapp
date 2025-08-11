from app.business.user.entities import User
from app.business.user.services.user_service import UserService
from app.core.utils.password import hash_password, verify_password

class AuthService:
    """
    Service for authentication operations.
    """
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def authenticate(self, username: str, password: str) -> User | None:
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

    def get_password_hash(self, password: str) -> str:
        """
        Get a password hash.
        
        Args:
            password: The password to hash
            
        Returns:
            The hashed password
        """
        return hash_password(password) 