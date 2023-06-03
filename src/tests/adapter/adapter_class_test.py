"""Test adapter module."""
from patterns.adapter.adapter_class import Adaptee, Adapter, Target


class TestAdapter:
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

    @staticmethod
    def test_adapter() -> None:
        """
        Test Adapter.

        Returns:
            None
        """

        adaptee = Adaptee()
        adapter = Adapter(adaptee)

        result = TestAdapter.client_code(adapter)
        assert result == "Specific behavior of the Adaptee."
