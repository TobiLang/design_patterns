"""Test Builder module."""
import pytest

from patterns.builder.builder import (
    ConcreteBuilderSportsCar,
    ConcreteBuilderSUV,
    Director,
)


# pylint: disable=too-few-public-methods
class TestBuilderSimple:
    """Test Builder module."""

    @pytest.fixture
    def director(self) -> Director:
        """
        Initialize Director class.

        Returns:
            Director
        """
        return Director()

    def test_construct_car_raise_exception(self, director: Director) -> None:
        """
        Raise an exception when trying to construct a car without a builder.

        Returns:
            None
        """
        with pytest.raises(ValueError):
            director.construct_car("Car", "Red", "V8", 4)

    def test_return_car_raise_exception(self, director: Director) -> None:
        """
        Raise an exception when trying to get a car without a builder.

        Returns:
            None
        """
        with pytest.raises(ValueError):
            director.get_car()

    @staticmethod
    def test_build_sportscar(director: Director) -> None:
        """
        Test building a car.

        Returns:
            None
        """
        # Construct a sports car
        sports_builder = ConcreteBuilderSportsCar()
        director.set_builder(sports_builder)
        director.construct_car("Car", "Red", "V8", 4)
        car = director.get_car()

        assert car.model == "Sports Car"
        assert car.color == "Vibrant Red"
        assert car.engine == "Powerful V8"
        assert car.wheels == 6
        assert str(car) == "Car: Model=Sports Car, Color=Vibrant Red, Engine=Powerful V8, Wheels=6"

    @staticmethod
    def test_build_suv(director: Director) -> None:
        """
        Test building a car.

        Returns:
            None
        """
        # Construct an SUV
        suv_builder = ConcreteBuilderSUV()
        director.set_builder(suv_builder)
        director.construct_car("BMW", "Blue", "V6", 4)
        car = director.get_car()

        assert car.model == "BMW SUV"
        assert car.color == "Blue"
        assert car.engine == "V6"
        assert car.wheels == 4
        assert str(car) == "Car: Model=BMW SUV, Color=Blue, Engine=V6, Wheels=4"
