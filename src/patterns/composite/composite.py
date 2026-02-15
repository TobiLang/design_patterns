"""Composite module."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """Abstract base class for all components in the composite pattern."""

    @abstractmethod
    def operation(self) -> str:
        """Execute the component's operation and return a string representation."""

    def add(self, component: "Component") -> None:
        """Add a component to the composite."""
        raise NotImplementedError(f"{self.__class__.__name__} does not support add().")

    def remove(self, component: "Component") -> None:
        """Remove a component from the composite."""
        raise NotImplementedError(f"{self.__class__.__name__} does not support remove().")

    def get_children(self) -> List["Component"]:
        """Return a list of children components."""
        return []


class Leaf(Component):
    """A leaf component that cannot have children."""

    def __init__(self, name: str) -> None:
        """Initialize a leaf with a name."""
        self._name = name

    def operation(self) -> str:
        """Return the leaf's name representation."""
        return f"Leaf({self._name})"


class Composite(Component):
    """A composite component that can contain other components."""

    def __init__(self, name: str) -> None:
        """Initialize a composite with a name and an empty list of children."""
        self._name = name
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        """Add a component to this composite."""
        self._children.append(component)

    def remove(self, component: Component) -> None:
        """Remove a component from this composite."""
        self._children.remove(component)

    def get_children(self) -> List[Component]:
        """Return a list of children components."""
        return self._children

    def operation(self) -> str:
        """Execute operation on all children and return the combined result."""
        results = [child.operation() for child in self._children]
        return f"Branch({self._name})[{', '.join(results)}]"


def client_code(component: Component) -> None:
    """The client treats Leaf and Composite uniformly."""
    print(component.operation())
