"""Class realizing the Singleton design pattern."""

from __future__ import annotations

from typing import Optional


# pylint: disable=too-few-public-methods
class Singleton:
    """Class realizing the Singleton design pattern."""

    _singleton: Optional[Singleton] = None

    def __init__(self) -> None:
        """
        Make sure that the constructor cannot be called from outside the class.
        """
        raise RuntimeError("Call get_instance() instead")

    @classmethod
    def get_instance(cls) -> Singleton:
        """
        Create and return the singleton instance.

        Returns:
            Singleton: Instance of the Singleton class
        """
        if cls._singleton is None:
            cls._singleton = cls.__new__(cls)
        return cls._singleton
