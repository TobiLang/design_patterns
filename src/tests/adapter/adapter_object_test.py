"""Test adapter module."""
from patterns.adapter.adapter_object import Adaptee, Adapter, Target


class TestAdapterObject:
    """Test adapter module."""

    @staticmethod
    def client_code(target: Target) -> str:
        """
        Mock client code that works with the target object via the target interface.

        Args:
            target: The target object.

        Returns:
            String
        """
        return target.request()

    def test_adapter(self) -> None:
        """
        Test Adapter via Object.

        Returns:
            None
        """

        adaptee = Adaptee()
        adapter = Adapter(adaptee)

        result = self.client_code(adapter)
        assert result == "Specific behavior of the Adaptee."
