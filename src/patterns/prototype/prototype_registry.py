"""Prototype Design Pattern implementation for shapes."""
import copy
from abc import ABC, abstractmethod
from typing import Dict, Optional


class Shape(ABC):
    """Abstract base class for all shapes."""

    def __init__(self, color: str) -> None:
        """
        Initialize shape with color.

        Args:
            color: The color of the shape.
        """
        self.color = color

    @abstractmethod
    def clone(self) -> "Shape":
        """
        Create a deep copy of the shape.

        Returns:
            A cloned instance of the shape.
        """

    @abstractmethod
    def draw(self) -> str:
        """
        Draw the shape.

        Returns:
            String representation of the shape.
        """


class Circle(Shape):
    """Circle shape implementation."""

    def __init__(self, color: str, radius: float) -> None:
        """
        Initialize a circle with color and radius.

        Args:
            color: The color of the circle.
            radius: The radius of the circle.
        """
        super().__init__(color)
        self.radius = radius

    def clone(self) -> "Circle":
        """
        Create a deep copy of the circle.

        Returns:
            A cloned Circle instance.
        """
        return copy.deepcopy(self)

    def draw(self) -> str:
        """
        Draw the circle.

        Returns:
            String representation of the circle.
        """
        return f"Circle(color={self.color}, radius={self.radius})"


class Rectangle(Shape):
    """Rectangle shape implementation."""

    def __init__(self, color: str, width: float, height: float) -> None:
        """
        Initialize the rectangle with color, width, and height.

        Args:
            color: The color of the rectangle.
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        super().__init__(color)
        self.width = width
        self.height = height

    def clone(self) -> "Rectangle":
        """
        Create a deep copy of the rectangle.

        Returns:
            A cloned Rectangle instance.
        """
        return copy.deepcopy(self)

    def draw(self) -> str:
        """
        Draw the rectangle.

        Returns:
            String representation of the rectangle.
        """
        return f"Rectangle(color={self.color}, width={self.width}, height={self.height})"


class ShapeRegistry:
    """Registry for shape prototypes."""

    def __init__(self) -> None:
        """Initialize an empty shape registry."""
        self._prototypes: Dict[str, Shape] = {}

    def register(self, name: str, prototype: Shape) -> None:
        """
        Register a shape prototype.

        Args:
            name: The name to register the prototype under.
            prototype: The shape prototype to register.
        """
        self._prototypes[name] = prototype

    def get(self, name: str) -> Shape:
        """
        Get a cloned shape by name.

        Args:
            name: The name of the registered prototype.

        Returns:
            A cloned instance of the requested shape.

        Raises:
            ValueError: If no prototype is registered under the given name.
        """
        prototype: Optional[Shape] = self._prototypes.get(name)
        if not prototype:
            raise ValueError(f"No prototype registered under '{name}'")
        return prototype.clone()


# Setup registry with baseline prototypes
registry = ShapeRegistry()
registry.register("small_red_circle", Circle(color="red", radius=5.0))
registry.register("large_blue_rectangle", Rectangle(color="blue", width=100.0, height=50.0))

# Client clones without knowing the concrete class
shape1 = registry.get("small_red_circle")
shape2 = registry.get("small_red_circle")
shape2.color = "green"  # customize the clone

print(shape1.draw())  # Output: Circle(color=red, radius=5.0)
print(shape2.draw())  # Output: Circle(color=green, radius=5.0)
