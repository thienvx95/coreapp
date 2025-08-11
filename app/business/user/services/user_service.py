from app.business.common.services.base import BaseService
from app.business.user.entities import User
from app.business.user.view_model.user_viewmodel import UserCreate, UserUpdate
from app.core.utils.password import hash_password


class UserService(BaseService[User, UserCreate, UserUpdate]):
    """
    Service for user operations.
    """
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

    async def add_role(self, user_id: str, role_name: str) -> User | None:
        """
        Add a role to a user.

        Args:
            user_id: The user ID
            role_name: The role name to add

        Returns:
            The updated user if found, None otherwise
        """
        user = await self.get(user_id)
        if not user:
            return None

        # Check if user already has this role
        if role_name in user.roles:
            return user

        # Add role to user's roles
        roles = user.roles.copy()
        roles.append(role_name)

        # Update user with new roles
        update_data = UserUpdate(roles=roles)
        return await self.update(user_id, update_data)

    async def remove_role(self, user_id: str, role_name: str) -> User | None:
        """
        Remove a role from a user.

        Args:
            user_id: The user ID
            role_name: The role name to remove

        Returns:
            The updated user if found, None otherwise
        """
        user = await self.get(user_id)
        if not user:
            return None

        # Check if user has this role
        if role_name not in user.roles:
            return user

        # Remove role from user's roles
        roles = [r for r in user.roles if r != role_name]

        # Update user with new roles
        update_data = UserUpdate(roles=roles)
        return await self.update(user_id, update_data)
