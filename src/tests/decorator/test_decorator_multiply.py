"""Test decorator module."""

from patterns.decorator.decorator_multiply import multiply_decorator


# pylint: disable=too-few-public-methods
class TestDecoratorMultiply:
    """Test decorator module."""

    @staticmethod
    def test_multiply() -> None:
        """
        Test that a function's output is multiplied by a factor.

        Returns:
            None
        """

        @multiply_decorator(2)
        def to_be_decorated(value_a: int, value_b: int) -> int:
            return value_a + value_b

        assert to_be_decorated(2, 3) == 10
