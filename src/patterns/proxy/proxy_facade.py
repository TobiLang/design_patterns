"""Module realizing the Proxy design pattern in combination with the Facade design pattern."""
import logging

from patterns.proxy.proxy import Subject


# pylint: disable=too-few-public-methods
class Facade:
    """
    Facade to simplify access to the subsystem.
    """

    def __init__(self, proxy: Subject) -> None:
        """
        Initialize Facade with proxy.

        Args:
            proxy: Proxy interface to change.

        Returns:
            None
        """
        self._proxy = proxy

    def operation(self) -> bool:
        """
        Simplify access to the subsystem.

        Returns:
            Boolean
        """
        logging.info("Accessing the subsystem..")

        result = self._proxy.do_action()
        if result:
            return True
        return False
