"""Facade module."""


# pylint: disable=too-few-public-methods


class SubsystemA:
    """Subsystem A component."""

    @staticmethod
    def operation_a() -> str:
        """Return operation A status."""
        return "Subsystem A: Ready!"


class SubsystemB:
    """Subsystem B component."""

    @staticmethod
    def operation_b() -> str:
        """Return operation B status."""
        return "Subsystem B: Ready!"


class SubsystemC:
    """Subsystem C component."""

    @staticmethod
    def operation_c() -> str:
        """Return operation C status."""
        return "Subsystem C: Fire!"


class Facade:
    """Facade pattern implementation to simplify subsystem interactions."""

    def __init__(self) -> None:
        """Initialize facade with all subsystems."""
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()
        self._subsystem_c = SubsystemC()

    def operation(self) -> str:
        """Execute operations on all subsystems and return combined results."""
        results = [
            "Facade initializes subsystems:",
            self._subsystem_a.operation_a(),
            self._subsystem_b.operation_b(),
            self._subsystem_c.operation_c(),
        ]
        return "\n".join(results)


# Client code
facade = Facade()
print(facade.operation())
