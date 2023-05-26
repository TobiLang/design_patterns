"""Module realizing the Proxy design pattern in combination with the Adapter design pattern."""

import logging

from patterns.proxy.proxy import Subject


# pylint: disable=too-few-public-methods
class Adapter:
    """
    Adapter to change RealSubject's interface.
    """

    def __init__(self, proxy: Subject) -> None:
        """
        Initialize Adapter with proxy.

        Args:
            proxy: Proxy interface to change.

        Returns:
            None
        """
        self._proxy = proxy

    def request(self) -> int:
        """
        Change the interface of RealSubject via Proxy.

        Returns:
            Integer
        """
        logging.info("Adapter: Changing the interface of RealSubject via Proxy.")
        self._proxy.do_action()
        return 1
