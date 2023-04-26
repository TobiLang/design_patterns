"""Decorators for text formatting."""
from typing import Callable


# pylint: disable=too-few-public-methods
class BoldDecorator:
    """
    Decorator that wraps the decorated function's output in <b> tags.
    """

    def __init__(self, func: Callable[[str], str]) -> None:
        """
        Initialize the decorator with the decorated function.

        Args:
            func: The decorated function.
        """
        self._func = func

    def __call__(self, *args: str, **kwargs: str) -> str:
        """
        Call the decorated function and wrap its output in <b> tags.

        Args:
            *args: The decorated function's positional arguments.
            **kwargs: The decorated function's keyword arguments.

        Returns:
            The decorated function's output wrapped in <b> tags.
        """
        return f"<b>{self._func(*args, **kwargs)}</b>"


class ItalicDecorator:
    """
    Decorator that wraps the decorated function's output in <i> tags.
    """

    def __init__(self, func: Callable[[str], str]) -> None:
        """
        Initialize the decorator with the decorated function.

        Args:
            func: The decorated function.
        """
        self._func = func

    def __call__(self, *args: str, **kwargs: str) -> str:
        """
        Call the decorated function and wrap its output in <i> tags.

        Args:
            *args: The decorated function's positional arguments.
            **kwargs: The decorated function's keyword arguments.

        Returns:
            The decorated function's output wrapped in <i> tags.
        """
        return f"<i>{self._func(*args, **kwargs)}</i>"
