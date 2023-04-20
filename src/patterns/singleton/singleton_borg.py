"""Singleton using Axel Martellis's Borg pattern."""
from typing import Any, Dict


# pylint: disable=too-few-public-methods
class Borg:
    """Borg class making class attributes global."""

    _shared_state: Dict[Any, Any] = {}

    def __init__(self) -> None:
        """
        Make it an attribute dictionary.
        """
        self.__dict__ = self._shared_state
