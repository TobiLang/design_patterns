"""Builder pattern module."""
from __future__ import annotations

from typing import Optional


class Director:
    """
    Director class.
    """

    def __init__(self) -> None:
        """
        Initialize Director class.
        """
        self.builder: Optional[Builder] = None

    def set_builder(self, builder: Builder) -> None:
        """
        Set the builder class.

        Args:
            builder: The builder class to be used by the director

        Returns:
            None
        """
        self.builder = builder

    def construct_car(self, model: str, color: str, engine: str, wheels: int) -> None:
        """
        Construct a car with the given parameters.

        Args:
            model: Car model to build
            color: Color of the car
            engine: Engine the car will have
            wheels: Number of wheels the car will have

        Returns:
            None
        """
        if self.builder is None:
            raise ValueError("Builder has not been set.")

        self.builder.set_model(model)
        self.builder.set_color(color)
        self.builder.set_engine(engine)
        self.builder.set_wheels(wheels)

    def get_car(self) -> Car:
        """
        Get the car that was built.

        Returns:
            Car
        """
        if self.builder is None:
            raise ValueError("Builder has not been set.")

        return self.builder.get_car()


class Builder:
    """
    Builder class.
    """

    def __init__(self) -> None:
        """
        Initialize Builder class with a car object (product).
        """
        self.car = Car()

    def set_model(self, model: str) -> None:
        """
        Set the model of the car.

        Args:
           model: Car model to build

        Returns:
            None
        """

    def set_color(self, color: str) -> None:
        """
        Set the color of the car.

        Args:
            color: Color of the car

        Returns:
            None
        """

    def set_engine(self, engine: str) -> None:
        """
        Set the engine of the car.

        Args:
             engine: Engine the car will have

        Returns:
            None
        """

    def set_wheels(self, wheels: int) -> None:
        """
        Set the number of wheels of the car.

        Args:
            wheels: Number of wheels the car will have

        Returns:
            None
        """

    def get_car(self) -> Car:
        """
        Get the car that was built.

        Returns:
            Car
        """
        return self.car


class ConcreteBuilderSportsCar(Builder):
    """
    Concrete Builder class for a sports car.
    """

    def set_model(self, model: str) -> None:
        """
        Set the model of the car as a sports model.

        Args:
            model: Car model to build

        Returns:
            None
        """
        self.car.model = f"Sports {model}"

    def set_color(self, color: str) -> None:
        """
        Set the color of the car as a vibrant color.
        Args:
            color: Color of the car

        Returns:
            None
        """
        self.car.color = f"Vibrant {color}"

    def set_engine(self, engine: str) -> None:
        """
        Set the engine of the car as a powerful engine.

        Args:
            engine: Engine the car will have

        Returns:
            None
        """
        self.car.engine = f"Powerful {engine}"

    def set_wheels(self, wheels: int) -> None:
        """
        Set the number of wheels of the sports car, more is better.

        Args:
            wheels: Number of wheels the car will have (plus some).

        Returns:
            None
        """
        self.car.wheels = wheels + 2


class ConcreteBuilderSUV(Builder):
    """
    Concrete Builder class for an SUV.
    """

    def set_model(self, model: str) -> None:
        """
        Set the model of the car as an SUV model.

        Args:
            model: Car model to build

        Returns:
            None
        """
        self.car.model = f"{model} SUV"

    def set_color(self, color: str) -> None:
        """
        Set the color of the car.
        Args:
            color: Color of the car

        Returns:
            None
        """
        self.car.color = color

    def set_engine(self, engine: str) -> None:
        """
        Set the engine of the car.

        Args:
            engine: Engine the car will have

        Returns:
            None
        """
        self.car.engine = engine

    def set_wheels(self, wheels: int) -> None:
        """
        Set the number of wheels of the car.

        Args:
            wheels: Number of wheels the car will have

        Returns:
            None
        """
        self.car.wheels = wheels


# pylint: disable=too-few-public-methods
class Car:
    """The Product class."""

    def __init__(self) -> None:
        """
        Initialize the Car class.
        """
        self.model: Optional[str] = None
        self.color: Optional[str] = None
        self.engine: Optional[str] = None
        self.wheels: Optional[int] = None

    def __str__(self) -> str:
        """
        String representation of the car.

        Returns:
            str
        """
        return f"Car: Model={self.model}, Color={self.color}, Engine={self.engine}, Wheels={self.wheels}"
