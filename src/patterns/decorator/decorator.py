"""Class realizing the Decorator design pattern."""

from abc import ABC, abstractmethod


class Coffee(ABC):
    """
    Abstract class representing a coffee.
    """

    @abstractmethod
    def get_cost(self) -> float:
        """
        Get the cost of the coffee.

        Returns:
            float: Cost of the coffee
        """

    @abstractmethod
    def get_description(self) -> str:
        """
        Get the description of the coffee.

        Returns:
            str: Description of the coffee
        """


class BasicCoffee(Coffee):
    """
    Concrete implementation of the coffee class representing a basic coffee.
    """

    def get_cost(self) -> float:
        """
        Get the cost of the coffee.

        Returns:
            float: Cost of the coffee
        """
        return 2.0

    def get_description(self) -> str:
        """
        Get the description of the coffee.

        Returns:
            str: Description of the coffee
        """
        return "Basic Coffee"


class CoffeeDecorator(Coffee):
    """
    Abstract class representing a decorator for a coffee.
    """

    def __init__(self, coffee: Coffee):
        """
        Initialize the decorator with a coffee.

        Args:
            coffee (Coffee): Coffee to decorate
        """
        self._coffee = coffee

    @abstractmethod
    def get_cost(self) -> float:
        """
        Get the cost of the coffee.

        Returns:
            float: Cost of the coffee
        """

    @abstractmethod
    def get_description(self) -> str:
        """
        Get the description of the coffee.

        Returns:
            str: Description of the coffee
        """


class MilkDecorator(CoffeeDecorator):
    """
    Concrete implementation of the coffee decorator class adding milk to a coffee.
    """

    def get_cost(self) -> float:
        """
        Adjust the cost of the coffee by adding the cost of milk.

        Returns:
            float: Cost of the coffee
        """
        return self._coffee.get_cost() + 0.5

    def get_description(self) -> str:
        """
        Adjust the description of the coffee by adding milk.

        Returns:
            str: Description of the coffee
        """
        return self._coffee.get_description() + ", Milk"


class SugarDecorator(CoffeeDecorator):
    """
    Concrete implementation of the coffee decorator class adding sugar to a coffee.
    """

    def get_cost(self) -> float:
        """
        Adjust the cost of the coffee by adding the cost of sugar.

        Returns:
            float: Cost of the coffee
        """
        return self._coffee.get_cost() + 0.25

    def get_description(self) -> str:
        """
        Adjust the description of the coffee by adding sugar.

        Returns:
            str: Description of the coffee
        """
        return self._coffee.get_description() + ", Sugar"
