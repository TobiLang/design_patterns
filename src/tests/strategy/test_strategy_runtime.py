"""Test Pricing Strategy module."""

import pytest

from patterns.strategy.strategy_runtime import (
    PRICING_STRATEGIES,
    CustomerType,
    EmployeePricing,
    Order,
    PremiumPricing,
    PricingStrategy,
    RegularPricing,
    WholesalePricing,
    get_pricing_strategy,
)


class TestPricingStrategies:
    """
    Test cases for the pricing strategy implementations.
    """

    base_price = 100.0

    def test_regular_pricing_calculate(self) -> None:
        """
        Test that RegularPricing returns the base price without a discount.

        Returns:
            None
        """
        strategy = RegularPricing()
        result = strategy.calculate(self.base_price)

        assert result == 100.0
        assert result == self.base_price

    def test_premium_pricing_calculate(self) -> None:
        """
        Test that PremiumPricing applies 20% discount correctly.

        Returns:
            None
        """
        strategy = PremiumPricing()
        result = strategy.calculate(self.base_price)

        assert result == 80.0
        assert result == self.base_price * 0.8

    def test_employee_pricing_calculate(self) -> None:
        """
        Test that EmployeePricing applies 50% discount correctly.

        Returns:
            None
        """
        strategy = EmployeePricing()
        result = strategy.calculate(self.base_price)

        assert result == 50.0
        assert result == self.base_price * 0.5

    def test_wholesale_pricing_calculate(self) -> None:
        """
        Test that WholesalePricing applies 40% discount correctly.

        Returns:
            None
        """
        strategy = WholesalePricing()
        result = strategy.calculate(self.base_price)

        assert result == 60.0
        assert result == self.base_price * 0.6

    def test_pricing_strategies_with_zero_price(self) -> None:
        """
        Test that all pricing strategies handle zero prices correctly.

        Returns:
            None
        """
        strategies = [RegularPricing(), PremiumPricing(), EmployeePricing(), WholesalePricing()]

        for strategy in strategies:
            result = strategy.calculate(0.0)
            assert result == 0.0

    def test_pricing_strategies_with_negative_price(self) -> None:
        """
        Test that all pricing strategies handle negative prices correctly.

        Returns:
            None
        """
        negative_price = -50.0

        regular = RegularPricing()
        premium = PremiumPricing()
        employee = EmployeePricing()
        wholesale = WholesalePricing()

        assert regular.calculate(negative_price) == -50.0
        assert premium.calculate(negative_price) == -40.0
        assert employee.calculate(negative_price) == -25.0
        assert wholesale.calculate(negative_price) == -30.0


class TestCustomerType:
    """
    Test cases for the CustomerType enum.
    """

    def test_customer_type_values(self) -> None:
        """
        Test that the CustomerType enum has the correct values.

        Returns:
            None
        """
        assert CustomerType.REGULAR.value == "regular"
        assert CustomerType.PREMIUM.value == "premium"
        assert CustomerType.EMPLOYEE.value == "employee"
        assert CustomerType.WHOLESALE.value == "wholesale"

    def test_customer_type_count(self) -> None:
        """
        Test that the CustomerType enum has exactly four members.

        Returns:
            None
        """
        assert len(CustomerType) == 4


class TestGetPricingStrategy:
    """
    Test cases for the get_pricing_strategy factory function.
    """

    def test_get_pricing_strategy_regular(self) -> None:
        """
        Test that get_pricing_strategy returns RegularPricing for a REGULAR customer type.

        Returns:
            None
        """
        strategy = get_pricing_strategy(CustomerType.REGULAR)

        assert isinstance(strategy, RegularPricing)
        assert strategy.calculate(100.0) == 100.0

    def test_get_pricing_strategy_premium(self) -> None:
        """
        Test that get_pricing_strategy returns PremiumPricing for a PREMIUM customer type.

        Returns:
            None
        """
        strategy = get_pricing_strategy(CustomerType.PREMIUM)

        assert isinstance(strategy, PremiumPricing)
        assert strategy.calculate(100.0) == 80.0

    def test_get_pricing_strategy_employee(self) -> None:
        """
        Test that get_pricing_strategy returns EmployeePricing for an EMPLOYEE customer type.

        Returns:
            None
        """
        strategy = get_pricing_strategy(CustomerType.EMPLOYEE)

        assert isinstance(strategy, EmployeePricing)
        assert strategy.calculate(100.0) == 50.0

    def test_get_pricing_strategy_wholesale(self) -> None:
        """
        Test that get_pricing_strategy returns WholesalePricing for a WHOLESALE customer type.

        Returns:
            None
        """
        strategy = get_pricing_strategy(CustomerType.WHOLESALE)

        assert isinstance(strategy, WholesalePricing)
        assert strategy.calculate(100.0) == 60.0

    def test_get_pricing_strategy_unknown_type_raises_error(self) -> None:
        """
        Test that get_pricing_strategy raises ValueError for an unknown customer type.

        Returns:
            None
        """
        original_strategies = PRICING_STRATEGIES.copy()
        PRICING_STRATEGIES.clear()

        try:
            with pytest.raises(ValueError) as exc_info:
                get_pricing_strategy(CustomerType.REGULAR)

            assert "Unbekannter Kundentyp" in str(exc_info.value)
        finally:
            PRICING_STRATEGIES.update(original_strategies)


class TestOrder:
    """
    Test cases for the Order class.
    """

    # pylint: disable=protected-access
    def test_order_initialization(self) -> None:
        """
        Test that Order initializes correctly with a pricing strategy.

        Returns:
            None
        """
        strategy = RegularPricing()
        order = Order(strategy)

        assert order._pricing == strategy

    def test_order_total_with_regular_pricing(self) -> None:
        """
        Test Order total method with RegularPricing strategy.

        Returns:
            None
        """
        strategy = RegularPricing()
        order = Order(strategy)

        result = order.total(100.0)

        assert result == 100.0

    def test_order_total_with_premium_pricing(self) -> None:
        """
        Test Order total method with PremiumPricing strategy.

        Returns:
            None
        """
        strategy = PremiumPricing()
        order = Order(strategy)

        result = order.total(100.0)

        assert result == 80.0

    def test_order_total_with_employee_pricing(self) -> None:
        """
        Test Order total method with EmployeePricing strategy.

        Returns:
            None
        """
        strategy = EmployeePricing()
        order = Order(strategy)

        result = order.total(100.0)

        assert result == 50.0

    def test_order_total_with_wholesale_pricing(self) -> None:
        """
        Test Order total method with WholesalePricing strategy.

        Returns:
            None
        """
        strategy = WholesalePricing()
        order = Order(strategy)

        result = order.total(200.0)

        assert result == 120.0


class TestStrategyPattern:
    """
    Test cases for the Strategy Pattern implementation.
    """

    base_price = 100.0

    def test_strategy_pattern_polymorphism(self) -> None:
        """
        Test that different pricing strategies can be used polymorphically.

        Returns:
            None
        """
        strategies = [RegularPricing(), PremiumPricing(), EmployeePricing(), WholesalePricing()]

        results = []
        for strategy in strategies:
            order = Order(strategy)
            results.append(order.total(self.base_price))

        assert all(isinstance(result, float) for result in results)
        assert len(set(results)) == 4
        assert results == [100.0, 80.0, 50.0, 60.0]

    def test_strategy_switching_with_factory_function(self) -> None:
        """
        Test that strategies can be obtained and used via factory function.

        Returns:
            None
        """
        customer_types = [CustomerType.REGULAR, CustomerType.PREMIUM, CustomerType.EMPLOYEE, CustomerType.WHOLESALE]

        expected_prices = [100.0, 80.0, 50.0, 60.0]

        for customer_type, expected_price in zip(customer_types, expected_prices):
            strategy = get_pricing_strategy(customer_type)
            order = Order(strategy)
            result = order.total(self.base_price)

            assert result == expected_price

    def test_pricing_registry_completeness(self) -> None:
        """
        Test that the pricing strategies registry contains all customer types.

        Returns:
            None
        """
        for customer_type in CustomerType:
            assert customer_type in PRICING_STRATEGIES
            strategy_class = PRICING_STRATEGIES[customer_type]
            assert issubclass(strategy_class, PricingStrategy)

    def test_strategy_interface_compliance(self) -> None:
        """
        Test that all pricing strategies implement the PricingStrategy interface.

        Returns:
            None
        """
        strategies = [RegularPricing(), PremiumPricing(), EmployeePricing(), WholesalePricing()]

        for strategy in strategies:
            assert isinstance(strategy, PricingStrategy)
            assert hasattr(strategy, "calculate")
            assert callable(getattr(strategy, "calculate"))

    def test_different_base_prices(self) -> None:
        """
        Test pricing strategies with different base prices.

        Returns:
            None
        """
        test_prices = [0.0, 1.0, 50.5, 99.99, 1000.0]

        for base_price in test_prices:
            regular = get_pricing_strategy(CustomerType.REGULAR)
            premium = get_pricing_strategy(CustomerType.PREMIUM)
            employee = get_pricing_strategy(CustomerType.EMPLOYEE)
            wholesale = get_pricing_strategy(CustomerType.WHOLESALE)

            assert regular.calculate(base_price) == base_price
            assert premium.calculate(base_price) == base_price * 0.8
            assert employee.calculate(base_price) == base_price * 0.5
            assert wholesale.calculate(base_price) == base_price * 0.6

    def test_pricing_accuracy_with_float_precision(self) -> None:
        """
        Test that pricing calculations maintain appropriate float precision.

        Returns:
            None
        """
        test_price = 33.33

        premium = PremiumPricing()
        employee = EmployeePricing()
        wholesale = WholesalePricing()

        premium_result = premium.calculate(test_price)
        employee_result = employee.calculate(test_price)
        wholesale_result = wholesale.calculate(test_price)

        assert round(premium_result, 2) == round(33.33 * 0.8, 2)
        assert round(employee_result, 2) == round(33.33 * 0.5, 2)
        assert round(wholesale_result, 2) == round(33.33 * 0.6, 2)
