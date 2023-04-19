"""Test singleton module."""

from patterns.singleton.singleton import Singleton


# pylint: disable=too-few-public-methods
class TestSingleton:
    """Test singleton module."""

    def test_uniqueness(self) -> None:
        """Test that only one instance of the singleton class is created.

        Returns:
            None
        """
        singleton1 = Singleton()
        singleton2 = Singleton()

        assert singleton1 is singleton2
