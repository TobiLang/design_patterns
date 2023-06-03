"""Test adapter module."""
from patterns.adapter.adapter_class import Adapter, Target


class TestAdapterClass:
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
        Test Adapter via Class.

        Returns:
            None
        """

        adapter = Adapter()

        result = self.client_code(adapter)
        assert result == "Specific behavior of the Adaptee."
