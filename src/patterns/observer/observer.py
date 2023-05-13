"""Observer Design Pattern."""
from abc import ABC, abstractmethod
from typing import Optional


# pylint: disable=too-few-public-methods
class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, data: str) -> None:
        """
        Receive update from subject.

        Args:
            data: String data from subject.

        Returns:
            None
        """


# pylint: disable=too-few-public-methods
class ConcreteObserver(Observer):
    """
    Concrete Observers react to the updates issued by the Subject they had been attached to.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a new observer.

        For the sake of simplicity, the Subject's state is stored.

        Args:
            name: Name of the observer (for logging purposes).
        """
        self._name = name
        self.state: Optional[str] = None

    def update(self, data: str) -> None:
        """
        Receive update from subject.

        Args:
            data: String data from subject.

        Returns:
            None
        """
        self.state = data
        print(f"{self._name} received data: {data}")


class Observable:
    """
    The Observable interface declares the methods of managing observers.
    """

    def __init__(self) -> None:
        """
        The list of observers. We can have multiple observers listening to.
        """
        self._observers = []

    def register_observer(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.

        Args:
            observer: A concrete observer to attach.

        Returns:
            None
        """
        self._observers.append(observer)

    def unregister_observer(self, observer: Observer) -> None:
        """
        Remove an observer from the subject.

        Args:
          observer: A concrete observer to detach.

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
            observer.update(data)


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
