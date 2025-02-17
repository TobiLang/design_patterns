"""Test factory module."""

from patterns.factory.simple_user_factory import (
    Permission,
    RoleType,
    UserRole,
    UserRoleFactory,
)


class TestSimpleUserFactory:
    """Test factory module."""

    def test_create_admin(self) -> None:
        """
        Test that the factory correctly creates an Admin instance.

        Returns:
            None
        """
        user_role = UserRoleFactory.create_role(RoleType.ADMIN)
        assert isinstance(user_role, UserRole)
        assert Permission.DELETE in user_role.get_permissions()

    def test_create_member(self) -> None:
        """
        Test that the factory correctly creates a Member instance.

        Returns:
            None
        """
        user_role = UserRoleFactory.create_role(RoleType.MEMBER)
        assert isinstance(user_role, UserRole)
        assert Permission.DELETE not in user_role.get_permissions()

    def test_create_guest(self) -> None:
        """
        Test that the factory correctly creates a Guest instance.

        Returns:
            None
        """
        user_role = UserRoleFactory.create_role(RoleType.GUEST)
        assert isinstance(user_role, UserRole)
        assert user_role.get_permissions() == [Permission.READ]

    def test_create_default(self) -> None:
        """
        Test that the factory correctly creates a Guest instance per default.

        Returns:
            None
        """
        user_role = UserRoleFactory.create_role("Unknown")
        assert isinstance(user_role, UserRole)
        assert user_role.get_permissions() == [Permission.READ]
