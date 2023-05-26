"""Module realizing the Proxy design pattern in combination with the Decorator design pattern."""


from patterns.proxy.proxy import Subject


# pylint: disable=too-few-public-methods
class Decorator:
    """
    Decorator to add new responsibilities to the proxy object without changing its interface.
    """

    def __init__(self, proxy: Subject) -> None:
        """
        Initialize Decorator with proxy.

        Args:
            proxy: Proxy interface to change.

        Returns:
            None
        """
        self._proxy = proxy

    def do_action(self) -> str:
        """
        Add new responsibilities to the proxy object without changing its interface.

        Returns:
            String
        """
        print("Decorator: Before request.")
        result = self._proxy.do_action()
        print("Decorator: After request.")

        return result
