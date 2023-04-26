"""Test decorator module."""

from patterns.decorator.decorator_texts import BoldDecorator, ItalicDecorator


class TextDecorator:
    """Test decorator module."""

    @staticmethod
    def test_bold_decorator() -> None:
        """
        Test that a function's output is wrapped in <b> tags.

        Returns:
            None
        """

        @BoldDecorator
        def to_be_decorated(name: str) -> str:
            return f"Hello, {name}!"

        formatted_greeting = to_be_decorated("John")
        assert formatted_greeting == "<b>Hello, John!</b>"

    @staticmethod
    def test_italic_decorator() -> None:
        """
        Test that a function's output is wrapped in <i> tags.

        Returns:
            None
        """

        @ItalicDecorator
        def to_be_decorated(name: str) -> str:
            return f"Hello, {name}!"

        formatted_greeting = to_be_decorated("John")
        assert formatted_greeting == "<i>Hello, John!</i>"
