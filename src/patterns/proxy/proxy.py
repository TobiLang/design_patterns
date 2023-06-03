"""Module realizing the Proxy design pattern."""

import logging
from abc import ABC, abstractmethod


# pylint: disable=too-few-public-methods
class Subject(ABC):
    """
    The Subject interface declares common operations for both RealSubject and the Proxy.
    """

    @abstractmethod
    def do_action(self) -> str:
        """
        The Subject interface declares a common method for both RealSubject and the Proxy.

        Returns:
            String
        """


# pylint: disable=too-few-public-methods
class RealSubject(Subject):
    """
    The RealSubject contains some core business logic.

    Usually, RealSubjects are capable of doing some useful work which may also be very slow or sensitive.
    """

    def do_action(self) -> str:
        """
        Work done by the RealSubject.

        The RealSubject can do some real work that is typically also very slow or
        sensitive - e.g. correcting input data.

        Returns:
            String
        """
        return "RealSubject: Handling request."


class Proxy(Subject):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, real_object: RealSubject) -> None:
        """
        The Proxy maintains a reference to an object of the RealSubject class.

        Args:
            real_object: RealSubject

        Returns:
            None
        """
        self._real_object = real_object

    def do_action(self) -> str:
        """
        Work done via the Proxy.

        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject.

        Returns:
            String
        """
        if self.check_access():
            self._real_object.do_action()
            self.log_access()

        return "Proxy: Handling request."

    def check_access(self) -> bool:
        """
        Helper function to check access rights before firing a real request.

        Returns:
            bool
        """
        logging.info("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        """
        Helper function to log access to the real subject.

        Returns:
            None
        """
        logging.info(
            "Proxy: Logged the time of request.",
        )
