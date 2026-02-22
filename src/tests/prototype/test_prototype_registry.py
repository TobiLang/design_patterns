"""Test prototype registry module."""

import pytest

from patterns.prototype.prototype_registry import Circle, Rectangle, ShapeRegistry


class TestShapeRegistry:
    """Test ShapeRegistry implementation."""

    def test_register_and_get_circle(self) -> None:
        """
        Test registering and retrieving a circle prototype.

        Returns:
            None
        """
        registry = ShapeRegistry()
        original_circle = Circle(color="red", radius=10.0)

        registry.register("test_circle", original_circle)
        cloned_circle = registry.get("test_circle")

        # Should be different objects
        assert original_circle is not cloned_circle

        # Should have same values
        assert original_circle.color == cloned_circle.color
        assert original_circle.radius == cloned_circle.radius
        assert isinstance(cloned_circle, Circle)

    def test_register_and_get_rectangle(self) -> None:
        """
        Test registering and retrieving a rectangle prototype.

        Returns:
            None
        """
        registry = ShapeRegistry()
        original_rectangle = Rectangle(color="blue", width=20.0, height=15.0)

        registry.register("test_rectangle", original_rectangle)
        cloned_rectangle = registry.get("test_rectangle")

        # Should be different objects
        assert original_rectangle is not cloned_rectangle

        # Should have same values
        assert original_rectangle.color == cloned_rectangle.color
        assert original_rectangle.width == cloned_rectangle.width
        assert original_rectangle.height == cloned_rectangle.height
        assert isinstance(cloned_rectangle, Rectangle)

    def test_clone_independence(self) -> None:
        """
        Test that cloned shapes are independent of the original.

        Returns:
            None
        """
        registry = ShapeRegistry()
        original_circle = Circle(color="green", radius=7.5)

        registry.register("independent_circle", original_circle)
        cloned_circle = registry.get("independent_circle")

        # Modify clone
        cloned_circle.color = "yellow"
        cloned_circle.radius = 12.0

        # Original should remain unchanged
        assert original_circle.color == "green"
        assert original_circle.radius == 7.5
        assert cloned_circle.color == "yellow"
        assert cloned_circle.radius == 12.0

    def test_get_nonexistent_prototype(self) -> None:
        """
        Test retrieving a non-existent prototype raises ValueError.

        Returns:
            None
        """
        registry = ShapeRegistry()

        with pytest.raises(ValueError, match="No prototype registered under 'nonexistent'"):
            registry.get("nonexistent")

    def test_multiple_clones_same_prototype(self) -> None:
        """
        Test creating multiple clones from the same registered prototype.

        Returns:
            None
        """
        registry = ShapeRegistry()
        original_shape = Rectangle(color="purple", width=30.0, height=40.0)

        registry.register("multi_clone", original_shape)

        clone1 = registry.get("multi_clone")
        clone2 = registry.get("multi_clone")
        clone3 = registry.get("multi_clone")

        # All should be different objects
        assert original_shape is not clone1
        assert original_shape is not clone2
        assert clone1 is not clone2
        assert clone1 is not clone3
        assert clone2 is not clone3

        # All should have same initial values
        assert original_shape.color == clone1.color == clone2.color == clone3.color
        assert original_shape.width == clone1.width == clone2.width == clone3.width
        assert original_shape.height == clone1.height == clone2.height == clone3.height

    def test_register_overwrite_prototype(self) -> None:
        """
        Test that registering with same name overwrites the previous prototype.

        Returns:
            None
        """
        registry = ShapeRegistry()

        # Register first prototype
        first_circle = Circle(color="red", radius=5.0)
        registry.register("overwrite_test", first_circle)

        # Register second prototype with same name
        second_circle = Circle(color="blue", radius=15.0)
        registry.register("overwrite_test", second_circle)

        # Should get the second prototype
        cloned_shape = registry.get("overwrite_test")
        assert cloned_shape.color == "blue"
        assert cloned_shape.radius == 15.0

    def test_draw_method_works_on_clones(self) -> None:
        """
        Test that draw method works correctly on cloned shapes.

        Returns:
            None
        """
        registry = ShapeRegistry()

        # Test Circle
        circle = Circle(color="orange", radius=3.5)
        registry.register("drawable_circle", circle)
        cloned_circle = registry.get("drawable_circle")

        expected_circle = "Circle(color=orange, radius=3.5)"
        assert cloned_circle.draw() == expected_circle

        # Test Rectangle
        rectangle = Rectangle(color="pink", width=8.0, height=12.0)
        registry.register("drawable_rectangle", rectangle)
        cloned_rectangle = registry.get("drawable_rectangle")

        expected_rectangle = "Rectangle(color=pink, width=8.0, height=12.0)"
        assert cloned_rectangle.draw() == expected_rectangle

    def test_empty_registry(self) -> None:
        """
        Test behavior of empty registry.

        Returns:
            None
        """
        registry = ShapeRegistry()

        with pytest.raises(ValueError, match="No prototype registered under 'anything'"):
            registry.get("anything")

    def test_registry_with_zero_dimensions(self) -> None:
        """
        Test registry with shapes having zero dimensions.

        Returns:
            None
        """
        registry = ShapeRegistry()

        # Circle with zero radius
        zero_circle = Circle(color="transparent", radius=0.0)
        registry.register("zero_circle", zero_circle)
        cloned_zero_circle = registry.get("zero_circle")

        assert cloned_zero_circle.radius == 0.0
        assert cloned_zero_circle.color == "transparent"

        # Rectangle with zero dimensions
        zero_rectangle = Rectangle(color="invisible", width=0.0, height=0.0)
        registry.register("zero_rectangle", zero_rectangle)
        cloned_zero_rectangle = registry.get("zero_rectangle")

        assert cloned_zero_rectangle.width == 0.0
        assert cloned_zero_rectangle.height == 0.0
        assert cloned_zero_rectangle.color == "invisible"

    def test_registry_with_negative_dimensions(self) -> None:
        """
        Test registry with shapes having negative dimensions.

        Returns:
            None
        """
        registry = ShapeRegistry()

        # Circle with negative radius
        negative_circle = Circle(color="weird", radius=-5.0)
        registry.register("negative_circle", negative_circle)
        cloned_negative_circle = registry.get("negative_circle")

        assert cloned_negative_circle.radius == -5.0
        assert cloned_negative_circle.color == "weird"

        # Rectangle with negative dimensions
        negative_rectangle = Rectangle(color="strange", width=-10.0, height=-20.0)
        registry.register("negative_rectangle", negative_rectangle)
        cloned_negative_rectangle = registry.get("negative_rectangle")

        assert cloned_negative_rectangle.width == -10.0
        assert cloned_negative_rectangle.height == -20.0
        assert cloned_negative_rectangle.color == "strange"

    def test_multiple_registries_independence(self) -> None:
        """
        Test that multiple registry instances are independent.

        Returns:
            None
        """
        registry1 = ShapeRegistry()
        registry2 = ShapeRegistry()

        # Register different shapes in each registry
        circle = Circle(color="red", radius=10.0)
        rectangle = Rectangle(color="blue", width=5.0, height=8.0)

        registry1.register("shape", circle)
        registry2.register("shape", rectangle)

        # Each registry should return its own registered prototype
        shape1 = registry1.get("shape")
        shape2 = registry2.get("shape")

        assert isinstance(shape1, Circle)
        assert isinstance(shape2, Rectangle)
        assert shape1.color == "red"
        assert shape2.color == "blue"
