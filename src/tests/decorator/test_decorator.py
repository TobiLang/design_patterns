"""Test decorator module."""

from patterns.decorator.decorator import BasicCoffee, MilkDecorator, SugarDecorator


class TestDecorator:
    """Test decorator module."""

    @staticmethod
    def test_coffee_with_milk() -> None:
        """Test that a coffee with milk is created.

        Returns:
            None
        """
        coffee = MilkDecorator(BasicCoffee())
        assert coffee.get_cost() == 2.5
        assert coffee.get_description() == "Basic Coffee, Milk"

    @staticmethod
    def test_coffee_with_milk_and_sugar() -> None:
        """Test that a coffee with milk and sugar is created.

        Returns:
            None
        """
        coffee = MilkDecorator(SugarDecorator(BasicCoffee()))
        assert coffee.get_cost() == 2.75
        assert coffee.get_description() == "Basic Coffee, Sugar, Milk"
