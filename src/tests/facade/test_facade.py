"""Test facade module."""

from patterns.facade.facade import Facade, SubsystemA, SubsystemB, SubsystemC


class TestFacade:
    """Test facade module."""

    @staticmethod
    def test_subsystem_a_operation() -> None:
        """Test that the SubsystemA operation returns a correct message.

        Returns:
            None
        """
        result = SubsystemA.operation_a()
        assert result == "Subsystem A: Ready!"

    @staticmethod
    def test_subsystem_b_operation() -> None:
        """Test that the SubsystemB operation returns the correct message.

        Returns:
            None
        """
        result = SubsystemB.operation_b()
        assert result == "Subsystem B: Ready!"

    @staticmethod
    def test_subsystem_c_operation() -> None:
        """Test that the SubsystemC operation returns the correct message.

        Returns:
            None
        """
        result = SubsystemC.operation_c()
        assert result == "Subsystem C: Fire!"

    @staticmethod
    def test_facade_operation() -> None:
        """Test that facade operation combines all subsystems correctly.

        Returns:
            None
        """
        facade = Facade()
        result = facade.operation()
        expected = "\n".join(
            ["Facade initializes subsystems:", "Subsystem A: Ready!", "Subsystem B: Ready!", "Subsystem C: Fire!"]
        )

        assert result == expected

    @staticmethod
    def test_facade_initialization() -> None:
        """Test that facade initializes with all subsystems.

        Returns:
            None
        """
        facade = Facade()
        # pylint: disable=protected-access
        assert hasattr(facade, "_subsystem_a")
        assert hasattr(facade, "_subsystem_b")
        assert hasattr(facade, "_subsystem_c")
        assert isinstance(facade._subsystem_a, SubsystemA)
        assert isinstance(facade._subsystem_b, SubsystemB)
        assert isinstance(facade._subsystem_c, SubsystemC)
