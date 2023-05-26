"""Test proxy module."""

from patterns.proxy.proxy import Proxy, Subject


class TestProxy:
    """Test proxy module."""

    @staticmethod
    def client_code(subject: Subject) -> str:
        """
        Mock client code that works with all objects implementing the Subject interface.

        The client code is supposed to work with all objects (both subjects and
        proxies) via the Subject interface in order to support both real subjects
        and proxies. In real life, however, clients mostly work with their real
        subjects directly. In this case, to implement the pattern more easily, you
        can extend your proxy from the real subject's class.
        Args:
            subject: RealSubject or Proxy

        Returns:
            String
        """
        return subject.do_action()

    def test_real_subject(self, real_subject: Subject) -> None:
        """
        Test real subject.

        Args:
            real_subject: RealSubject

        Returns:
            None
        """
        result = self.client_code(real_subject)

        assert result == "RealSubject: Handling request."

    def test_proxy(self, real_subject: Subject) -> None:
        """
        Test proxy.

        Args:
             real_subject: RealSubject

        Returns:
            None
        """
        proxy = Proxy(real_subject)

        result = self.client_code(proxy)

        assert result == "Proxy: Handling request."
