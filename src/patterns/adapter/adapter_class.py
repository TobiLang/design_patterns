"""Adapter pattern module."""


# pylint: disable=too-few-public-methods
class Target:
    """
    The Target is the interface that our client code understands.
    """

    def request(self) -> str:
        """
        The default target's behavior.

        Returns:
            str: The expected result.
        """
        return "Target: The default target's behavior."


# pylint: disable=too-few-public-methods
class Adaptee:
    """
    The Adaptee is the class we want to use, but its interface is incompatible with the existing client code.
    """

    def specific_request(self) -> str:
        """
        Defines the specific behavior of the Adaptee.

        Returns:
            str: The expected result.
        """
        return "Specific behavior of the Adaptee."


# pylint: disable=too-few-public-methods
class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's interface.

    It inherits from both the Target and the Adaptee classes.
    """

    def request(self) -> str:
        """
        The Adapter uses the Adaptee's interface to call its specific behavior.

        Returns:
            str: The expected result.
        """
        return self.specific_request()
