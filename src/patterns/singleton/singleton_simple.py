"""Class realising the Singleton design pattern."""

from __future__ import annotations

from typing import Any, Optional


# pylint: disable=too-few-public-methods
class SingletonSimple:
    """Class realising the Singleton design pattern using a class attribute."""

    _instance: Optional[SingletonSimple] = None

    @classmethod
    def __new__(cls, *args: Any, **kwargs: Any) -> SingletonSimple:
        """
        Create and return the singleton instance.

        Args:
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            SingletonSimple: Instance of the SingletonSimple class
        """
        if cls._instance is None:
            cls._instance = super().__new__(*args, **kwargs)
        return cls._instance
