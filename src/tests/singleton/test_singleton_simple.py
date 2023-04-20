"""Test singleton module."""

from patterns.singleton.singleton_simple import SingletonSimple


# pylint: disable=too-few-public-methods
class TestSingletonSimple:
    """Test singleton module."""

    def test_uniqueness(self) -> None:
        """Test that only one instance of the singleton class is created.

        Returns:
            None
        """
        singleton1 = SingletonSimple()
        singleton2 = SingletonSimple()

        assert singleton1 is singleton2
