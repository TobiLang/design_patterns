"""Test proxy module."""

from patterns.proxy.proxy import Proxy, Subject
from patterns.proxy.proxy_facade import Facade


class TestProxyFacade:
    """Test proxy module."""

    @staticmethod
    def client_code(facade: Facade) -> bool:
        """
        Mock client code that works with all objects implementing the Facade pattern.

        Args:
            facade: Facade to change RealSubject's interface

        Returns:
            bool
        """
        return facade.operation()

    def test_proxy_facade(self, real_subject: Subject) -> None:
        """
        Test proxy with facade.

        Args:
             real_subject: RealSubject

        Returns:
            None
        """
        proxy = Proxy(real_subject)
        facade = Facade(proxy)

        result = self.client_code(facade)

        assert result is True
