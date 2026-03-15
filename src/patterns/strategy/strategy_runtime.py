"""Pricing Strategy module."""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Type


class CustomerType(Enum):
    """
    An enum representing the different types of customers.

    Attributes:
        REGULAR: Regular customer with no discount
        PREMIUM: Premium customer with 20% discount
        EMPLOYEE: Employee with 50% discount
        WHOLESALE: Wholesale customer with 40% discount
    """

    REGULAR = "regular"
    PREMIUM = "premium"
    EMPLOYEE = "employee"
    WHOLESALE = "wholesale"


# pylint: disable=too-few-public-methods
class PricingStrategy(ABC):
    """Abstract base class for different pricing strategies."""

    @abstractmethod
    def calculate(self, base_price: float) -> float:
        """
        Calculates the price based on the base price and the strategy.

        Args:
            base_price: The base price of the product

        Returns:
            Discounted price
        """


# pylint: disable=too-few-public-methods
class RegularPricing(PricingStrategy):
    """Regular price strategy with no discount."""

    def calculate(self, base_price: float) -> float:
        """
        Calculates the regular price without any discount.

        Args:
            base_price: The base price of the product

        Returns:
            The regular price without any discount
        """
        return base_price


# pylint: disable=too-few-public-methods
class PremiumPricing(PricingStrategy):
    """Premium price strategy with 20% discount."""

    def calculate(self, base_price: float) -> float:
        """
        Calculates the price with a 20% discount.

        Args:
            base_price: The base price of the product

        Returns:
            The price with a 20% discount
        """
        return base_price * 0.8


# pylint: disable=too-few-public-methods
class EmployeePricing(PricingStrategy):
    """Employee price strategy with a 50% discount."""

    def calculate(self, base_price: float) -> float:
        """
        Calculates the price with a 50% discount.

        Args:
            base_price: The base price of the product

        Returns:
            The price with a 50% discount
        """
        return base_price * 0.5


# pylint: disable=too-few-public-methods
class WholesalePricing(PricingStrategy):
    """Wholesale price strategy with a 40% discount."""

    def calculate(self, base_price: float) -> float:
        """
        Calculates the price with a 40% discount.

        Args:
            base_price: The base price of the product

        Returns:
            The price with a 40% discount
        """
        return base_price * 0.6


# Strategy registry für die Auflösung zur Laufzeit
PRICING_STRATEGIES: Dict[CustomerType, Type[PricingStrategy]] = {
    CustomerType.REGULAR: RegularPricing,
    CustomerType.PREMIUM: PremiumPricing,
    CustomerType.EMPLOYEE: EmployeePricing,
    CustomerType.WHOLESALE: WholesalePricing,
}


def get_pricing_strategy(c_type: CustomerType) -> PricingStrategy:
    """
    Returns the appropriate PricingStrategy instance based on the customer type.

    Args:
        c_type: The type of customer (e.g., CustomerType.REGULAR)

    Returns:
        An instance of the appropriate PricingStrategy class

    Raises:
        ValueError: For an unknown customer type
    """
    strategy_class = PRICING_STRATEGIES.get(c_type)
    if not strategy_class:
        raise ValueError(f"Unbekannter Kundentyp: '{c_type}'")
    return strategy_class()


# pylint: disable=too-few-public-methods
class Order:
    """Represents a single order with a specific pricing strategy."""

    def __init__(self, pricing: PricingStrategy) -> None:
        """
        Initialises a new Order instance with the given pricing strategy.

        Args:
            pricing: The pricing strategy to apply to the order
        """
        self._pricing = pricing

    def total(self, base_price: float) -> float:
        """
        Calculates the total price based on the given base price and the pricing strategy.

        Args:
            base_price: Regular price of the product

        Returns:
            Final price after applying the pricing strategy
        """
        return self._pricing.calculate(base_price)
