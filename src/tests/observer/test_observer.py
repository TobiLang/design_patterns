"""Test observer module."""
from patterns.observer.observer import ConcreteObserver, ConcreteSubject


# pylint: disable=too-few-public-methods
class TestObserver:
    """Test observer module."""

    @staticmethod
    def test_observer() -> None:
        """Validate correct communication between observers and subject.

        Returns:
            None
        """
        # Setup subject and observers
        subject = ConcreteSubject()
        observer1 = ConcreteObserver("Observer1")
        observer2 = ConcreteObserver("Observer2")

        # Register observers to subject
        subject.register_observer(observer1)
        subject.register_observer(observer2)

        # Update subject state. Should notify all observers.
        subject.set_state("Hello, Observers!")

        assert observer1.state == "Hello, Observers!"
        assert observer2.state == "Hello, Observers!"
