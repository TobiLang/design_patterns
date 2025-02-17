"""Factory module."""
from abc import ABC, abstractmethod

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
    Concrete implementation of the Animal class representing a dog.
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
    Concrete implementation of the Animal class representing a cat.
    """

    def speak(self) -> str:
        """
        Let the animal speak its catchphrase.

        Returns:
            str: Catchphrase of the animal.
        """
        return "Meow!"


class AnimalCreator(ABC):
    """
    Abstract Creator that declares the factory method.
    """

    @abstractmethod
    def create_animal(self) -> Animal:
        """
        Factory method to create an animal.

        Returns:
            Animal: The created animal instance.
        """


class DogFactory(AnimalCreator):
    """
    Dog Factory class implementing the AnimalCreator interface.
    """

    def create_animal(self) -> Animal:
        """
        Factory method to create a dog.

        Returns:
            Dog: The created dog instance.
        """
        return Dog()


class CatFactory(AnimalCreator):
    """
    Cat Factory class implementing the AnimalCreator interface.
    """

    def create_animal(self) -> Animal:
        """
        Factory method to create a cat.

        Returns:
            Cat: The created cat instance.
        """
        return Cat()


# Client code
dog_factory = DogFactory()
cat_factory = CatFactory()

dog = dog_factory.create_animal()
cat = cat_factory.create_animal()

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
