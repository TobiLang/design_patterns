"""Class realising the Singleton design pattern."""

from __future__ import annotations

from typing import Any


# pylint: disable=too-few-public-methods
class Singleton:
    """Class realising the Singleton design pattern."""

    _instance = None

    @classmethod
    def __new__(cls, *args: Any, **kwargs: Any) -> Singleton:
        """
        Implement the Singleton pattern. Only create a new object in case it does not already exist.

        Args:
            *args: Positional arguments
            **kwargs: Keyword arguments
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
