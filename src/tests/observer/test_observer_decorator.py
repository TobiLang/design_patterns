"""Test observer module."""
from typing import Optional

from patterns.observer.observer_decorator import ConcreteSubject


# pylint: disable=too-few-public-methods
class TestObserverDecorator:
    """Test observer module."""

    def test_observer(self) -> None:
        """Validate correct communication between observers and subject.

        Returns:
            None
        """
        # Setup state
        # This is a workaround to be able to access the state of the observers and make it testable
        state_1: Optional[str] = None
        state_2: Optional[str] = None

        # Setup subject
        subject = ConcreteSubject()

        # Create observers and register them to the subject via a decorator
        @subject.observer
        def observer1(data: str) -> None:
            """
            Handle data received from subject.

            Args:
                data: String data from subject.

            Returns:
                None
            """
            nonlocal state_1
            state_1 = data
            print(f"Observer1 received data: {data}")

        @subject.observer
        def observer2(data: str) -> None:
            """
            Handle data received from subject.
            Args:
                data: String data from subject.

            Returns:
                None
            """
            nonlocal state_2
            state_2 = data
            print(f"Observer2 received data: {data}")

        # Update subject state. Should notify all observers.
        subject.set_state("Hello, Observers!")

        assert state_1 == "Hello, Observers!"
        assert state_2 == "Hello, Observers!"
