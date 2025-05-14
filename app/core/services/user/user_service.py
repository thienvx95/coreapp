from app.core.services.base import BaseService
from app.core.repository.base import BaseRepository
from app.models.user import User
from app.core.viewmodels.user.user_viewmodel import UserCreate, UserUpdate
from app.core.utils.password import hash_password
from motor.motor_asyncio import AsyncIOMotorDatabase

class UserService(BaseService[User, UserCreate, UserUpdate]):
    """
    Service for user operations.
    """
    def __init__(self, db: AsyncIOMotorDatabase):
        repository = BaseRepository(db, "users", User)
        super().__init__(repository)
        self.repository = repository

    async def create(self, obj_in: UserCreate) -> User:
        """
        Create a new user.
        
        Args:
            obj_in: The user data
            
        Returns:
            The created user
        """
        # Hash the password
        obj_in.password = hash_password(obj_in.password)
        return await super().create(obj_in)

    async def update(self, id: str, obj_in: UserUpdate) -> User | None:
        """
        Update a user.
        
        Args:
            id: The user ID
            obj_in: The user data to update
            
        Returns:
            The updated user if found, None otherwise
        """
        # Hash the password if it's being updated
        if obj_in.password:
            obj_in.password = hash_password(obj_in.password)
        return await super().update(id, obj_in)

    async def get_by_email(self, email: str) -> User | None:
        """
        Get a user by email.
        
        Args:
            email: The user's email
            
        Returns:
            The user if found, None otherwise
        """
        return await self.repository.find_one({"email": email})

    async def get_by_username(self, username: str) -> User | None:
        """
        Get a user by username.
        
        Args:
            username: The user's username
            
        Returns:
            The user if found, None otherwise
        """
        return await self.repository.find_one({"username": username}) 