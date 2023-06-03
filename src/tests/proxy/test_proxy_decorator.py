"""Test proxy module."""

from patterns.proxy.proxy import Proxy, Subject
from patterns.proxy.proxy_decorator import Decorator


class TestProxyAdapter:
    """Test proxy module."""

    @staticmethod
    def client_code(decorator: Decorator) -> str:
        """
        Mock client code that works with all objects implementing the Decorator.

        Args:
            decorator: Decorator to add new responsibilities to the proxy object without changing its interface.

        Returns:
            String
        """
        return decorator.do_action()

    def test_proxy_decorator(self, real_subject: Subject) -> None:
        """
        Test proxy with decorator.

        Args:
             real_subject: RealSubject

        Returns:
            None
        """
        proxy = Proxy(real_subject)
        decorator = Decorator(proxy)
        result = self.client_code(decorator)

        assert result == "Proxy: Handling request."
