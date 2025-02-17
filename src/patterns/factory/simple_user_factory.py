"""Factory module."""
from abc import ABC, abstractmethod
from enum import Enum
from typing import List

# pylint: disable=too-few-public-methods


class Permission(Enum):
    """Permissions available for users."""

    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"


class UserRole(ABC):
    """Abstract class representing a user."""

    @abstractmethod
    def get_permissions(self) -> List[Permission]:
        """
        Retrieve the permissions of the user.

        Returns:
            list: List of permissions.
        """


class Admin(UserRole):
    """Subclass representing an Admin role."""

    def get_permissions(self) -> List[Permission]:
        """
        Retrieve the permissions of the Admin user.

        Returns:
            list: List of permissions.
        """
        return [Permission.CREATE, Permission.READ, Permission.UPDATE, Permission.DELETE]


class Member(UserRole):
    """Subclass representing a Member role."""

    def get_permissions(self) -> List[Permission]:
        """
        Retrieve the permissions of the Member user.

        Returns:
            list: List of permissions.
        """
        return [Permission.CREATE, Permission.READ, Permission.UPDATE]


class Guest(UserRole):
    """Subclass representing a Guest role."""

    def get_permissions(self) -> List[Permission]:
        """
        Retrieve the permissions of the Guest user.

        Returns:
            list: List of permissions.
        """
        return [Permission.READ]


class RoleType(Enum):
    """Types of roles."""

    ADMIN = "Admin"
    MEMBER = "Member"
    GUEST = "Guest"


class UserRoleFactory:
    """Factory class to create user roles."""

    @staticmethod
    def create_role(role_type: RoleType) -> UserRole:
        """
        Create a user role instance based on the type provided.

        Args:
            role_type (RoleType): The type of role to create (e.g., 'Admin', 'Member', 'Guest').

        Returns:
            UserRole: An instance of the specified role.
        """
        if role_type == RoleType.ADMIN:
            return Admin()
        if role_type == RoleType.MEMBER:
            return Member()
        return Guest()
