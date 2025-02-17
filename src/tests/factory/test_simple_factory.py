"""Test factory module."""
import pytest

from patterns.factory.simple_factory import Animal, AnimalFactory, AnimalType


class TestSimpleFactory:
    """Test factory module."""

    def test_create_dog(self) -> None:
        """
        Test that the factory correctly creates a Dog instance.

        Returns:
            None
        """
        animal = AnimalFactory.create_animal(AnimalType.DOG)
        assert isinstance(animal, Animal)
        assert animal.speak() == "Woof!"

    def test_create_cat(self) -> None:
        """
        Test that the factory correctly creates a Cat instance.

        Returns:
            None
        """
        animal = AnimalFactory.create_animal(AnimalType.CAT)
        assert isinstance(animal, Animal)
        assert animal.speak() == "Meow!"

    def test_create_animal_raise_exception(self) -> None:
        """
        Raise an exception when trying to create an Animal of unknown type.

        Returns:
            None
        """
        with pytest.raises(ValueError):
            AnimalFactory.create_animal("Unknown")
