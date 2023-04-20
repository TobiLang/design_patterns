"""Test singleton module."""
from patterns.singleton.singleton_borg import Borg


# pylint: disable=too-few-public-methods
class TestSingletonBorg:
    """Test singleton module."""

    def test_uniqueness(self) -> None:
        """Test that only one instance of the singleton class is created.

        Returns:
            None
        """
        borg1 = Borg()
        borg2 = Borg()

        borg1.x_value = 42

        assert borg1 is not borg2
        assert borg1.x_value == borg2.x_value
