"""Adapter pattern module."""

from abc import ABC, abstractmethod


# pylint: disable=too-few-public-methods
class Target(ABC):
    """
    The Target defines the interface used and expected by the client.
    """

    @abstractmethod
    def request(self) -> str:
        """
        Defines the interface used by the client.

        Returns:
            str: The expected result.
        """


# pylint: disable=too-few-public-methods
class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible with the existing client code.
    """

    def specific_request(self) -> str:
        """
        Defines the specific behavior of the Adaptee.

        Returns:
            str: The expected result.
        """
        return "Specific behavior of the Adaptee."


# pylint: disable=too-few-public-methods
class Adapter(Target):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's interface.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        """
        Initialize the Adapter with the adaptee class to wrap.

        Args:
            adaptee: The adaptee class to wrap.
        """
        self.adaptee = adaptee

    def request(self) -> str:
        """
        The Adapter uses the Adaptee's interface to call its specific behavior.

        Returns:
            str: The expected result.
        """
        return self.adaptee.specific_request()
