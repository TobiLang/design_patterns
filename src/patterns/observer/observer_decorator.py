"""Observer Design Pattern."""

from typing import Callable, List, Optional


class Observable:
    """
    The Observable interface declares the methods of managing observers.
    """

    def __init__(self) -> None:
        """
        The list of observers. We can have multiple observers listening to.
        """
        self._observers: List[Callable[[str], None]] = []

    def register_observer(self, observer: Callable[[str], None]) -> None:
        """
        Attach an observer to the subject.

        Args:
            observer: An observer function to attach.

        Returns:
            None
        """
        self._observers.append(observer)

    def unregister_observer(self, observer: Callable[[str], None]) -> None:
        """
        Remove an observer from the subject.

        Args:
          observer: An observer function to detach.

        Returns:
            None
        """
        self._observers.remove(observer)

    def notify_observers(self, data: str) -> None:
        """
        Notify all observers about an event.

        Args:
            data: Data to send to observers.

        Returns:
            None
        """
        for observer in self._observers:
            observer(data)

    def observer(self, func: Callable[[str], None]) -> Callable[[str], None]:
        """
        Decorator to register a function as an observer.

        Args:
            func: Function to register as an observer.

        Returns:
            Function: The same function that was passed as an argument.
        """
        self.register_observer(func)
        return func


# pylint: disable=duplicate-code
class ConcreteSubject(Observable):
    """
    The Subject owns some important state and notifies observers when the state changes.
    """

    def __init__(self) -> None:
        """
        Initialize a new subject.

        For the sake of simplicity, the Subject's state, essential to all subscribers, is stored.
        """
        self._state: Optional[str] = None
        super().__init__()

    def set_state(self, data: str) -> None:
        """
        Set the state of the subject and notify all observers.

        Args:
            data:

        Returns:
            None
        """
        self._state = data
        self.notify_observers(data)
