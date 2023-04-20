"""Test singleton module."""
import pytest

from patterns.singleton.singleton import Singleton


# pylint: disable=too-few-public-methods
class TestSingleton:
    """Test singleton module."""

    def test_raises_runtime_error(self) -> None:
        """Test that a Runtime Error is raised when trying to instantiate the class.

        Returns:
            None
        """
        with pytest.raises(RuntimeError):
            Singleton()

    def test_uniqueness(self) -> None:
        """Test that only one instance of the singleton class is created.

        Returns:
            None
        """
        singleton1 = Singleton.get_instance()
        singleton2 = Singleton.get_instance()

        assert singleton1 is singleton2
