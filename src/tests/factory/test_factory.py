"""Test factory module."""

from patterns.factory.factory import Animal, AnimalCreator, CatFactory, DogFactory


class TestFactory:
    """Test factory module."""

    def test_dog_factory_creates_dog(self) -> None:
        """
        Test to ensure DogFactory correctly creates a Dog instance.

        Returns:
            None
        """
        dog_factory = DogFactory()
        animal = dog_factory.create_animal()
        assert isinstance(dog_factory, AnimalCreator)
        assert isinstance(animal, Animal)
        assert animal.speak() == "Woof!"

    def test_cat_factory_creates_cat(self) -> None:
        """
        Test to ensure CatFactory correctly creates a Cat instance.

        Returns:
            None
        """
        cat_factory = CatFactory()
        animal = cat_factory.create_animal()
        assert isinstance(cat_factory, AnimalCreator)
        assert isinstance(animal, Animal)
        assert animal.speak() == "Meow!"
