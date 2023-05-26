"""Test proxy module."""

from patterns.proxy.proxy import Proxy, Subject
from patterns.proxy.proxy_adapter import Adapter


class TestProxyAdapter:
    """Test proxy module."""

    @staticmethod
    def client_code(adapter: Adapter) -> str:
        """
        Mock client code that works with all objects implementing the Adapter.

        Args:
            adapter: Adapter to change RealSubject's interface

        Returns:
            String
        """
        return adapter.request()

    def test_proxy_adapter(self, real_subject: Subject) -> None:
        """
        Test proxy with adapter.

        Args:
             real_subject: RealSubject

        Returns:
            None
        """
        proxy = Proxy(real_subject)
        adapter = Adapter(proxy)

        result = self.client_code(adapter)

        assert result == 1
