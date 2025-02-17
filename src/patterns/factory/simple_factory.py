"""Factory module."""
from abc import ABC, abstractmethod
from enum import Enum

# pylint: disable=too-few-public-methods


class Animal(ABC):
    """
    Abstract class representing an animal.
    """

    @abstractmethod
    def speak(self) -> str:
        """
        Let the animal speak its catchphrase.

        Returns:
            str: Catchphrase of the animal.
        """


class Dog(Animal):
    """
    Concrete implementation of the animal class representing a dog.
    """

    def speak(self) -> str:
        """
        Let the animal speak its catchphrase.

        Returns:
            str: Catchphrase of the animal.
        """
        return "Woof!"


class Cat(Animal):
    """
    Concrete implementation of the animal class representing a cat.
    """

    def speak(self) -> str:
        """
        Let the animal speak its catchphrase.

        Returns:
            str: Catchphrase of the animal.
        """
        return "Meow!"


class AnimalType(Enum):
    """Types of animals."""

    DOG = "Dog"
    CAT = "Cat"


class AnimalFactory:
    """
    Factory class for creating animals.
    """

    @staticmethod
    def create_animal(animal_type: AnimalType) -> Animal:
        """
        Create an animal based on the given type.

        Args:
            animal_type (AnimalType): Type of the animal to create.

        Returns:
            Animal: Created animal.

        Raises:
            ValueError: for invalid animal_type.
        """
        if animal_type == AnimalType.DOG:
            return Dog()
        if animal_type == AnimalType.CAT:
            return Cat()
        raise ValueError("Invalid animal type")


# Client code
animal1 = AnimalFactory.create_animal(AnimalType.DOG)
animal2 = AnimalFactory.create_animal(AnimalType.CAT)
print(animal1.speak())  # Output: Woof!
print(animal2.speak())  # Output: Meow!
