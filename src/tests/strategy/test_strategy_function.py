"""Test functional strategy module."""

from io import StringIO
from unittest.mock import patch

from patterns.strategy.strategy_function import (
    ProductCatalog,
    sort_by_name,
    sort_by_price_asc,
    sort_by_price_desc,
    sort_by_rating,
)


class TestSortingStrategies:
    """
    Test cases for the sorting strategy functions.
    """

    test_products = [
        {"name": "Keyboard", "price": 89.99, "rating": 4.5},
        {"name": "Mouse", "price": 49.99, "rating": 4.8},
        {"name": "Monitor", "price": 349.99, "rating": 4.2},
        {"name": "Headset", "price": 129.99, "rating": 4.6},
    ]

    def test_sort_by_name(self) -> None:
        """
        Test that sort_by_name sorts products alphabetically by name.

        Returns:
            None
        """
        result = sort_by_name(self.test_products)

        expected_order = ["Headset", "Keyboard", "Monitor", "Mouse"]
        actual_order = [product["name"] for product in result]

        assert actual_order == expected_order

    def test_sort_by_price_asc(self) -> None:
        """
        Test that sort_by_price_asc sorts products by price in ascending order.

        Returns:
            None
        """
        result = sort_by_price_asc(self.test_products)

        expected_prices = [49.99, 89.99, 129.99, 349.99]
        actual_prices = [product["price"] for product in result]

        assert actual_prices == expected_prices

    def test_sort_by_price_desc(self) -> None:
        """
        Test that sort_by_price_desc sorts products by price in descending order.

        Returns:
            None
        """
        result = sort_by_price_desc(self.test_products)

        expected_prices = [349.99, 129.99, 89.99, 49.99]
        actual_prices = [product["price"] for product in result]

        assert actual_prices == expected_prices

    def test_sort_by_rating(self) -> None:
        """
        Test that sort_by_rating sorts products by rating in descending order.

        Returns:
            None
        """
        result = sort_by_rating(self.test_products)

        expected_ratings = [4.8, 4.6, 4.5, 4.2]
        actual_ratings = [product["rating"] for product in result]

        assert actual_ratings == expected_ratings

    def test_sorting_preserves_original_data(self) -> None:
        """
        Test that sorting functions don't modify the original data.

        Returns:
            None
        """
        original_products = self.test_products.copy()

        sort_by_name(self.test_products)
        sort_by_price_asc(self.test_products)
        sort_by_price_desc(self.test_products)
        sort_by_rating(self.test_products)

        assert self.test_products == original_products

    def test_sorting_empty_list(self) -> None:
        """
        Test that all sorting functions handle empty lists correctly.

        Returns:
            None
        """
        empty_list = []

        assert sort_by_name(empty_list) == []
        assert sort_by_price_asc(empty_list) == []
        assert sort_by_price_desc(empty_list) == []
        assert sort_by_rating(empty_list) == []

    def test_sorting_single_item(self) -> None:
        """
        Test that all sorting functions handle single-item lists correctly.

        Returns:
            None
        """
        single_item = [{"name": "Test", "price": 100.0, "rating": 3.0}]

        assert sort_by_name(single_item) == single_item
        assert sort_by_price_asc(single_item) == single_item
        assert sort_by_price_desc(single_item) == single_item
        assert sort_by_rating(single_item) == single_item


class TestProductCatalog:
    """
    Test cases for the ProductCatalog class.
    """

    test_products = [
        {"name": "Keyboard", "price": 89.99, "rating": 4.5},
        {"name": "Mouse", "price": 49.99, "rating": 4.8},
        {"name": "Monitor", "price": 349.99, "rating": 4.2},
    ]

    # pylint: disable=protected-access
    def test_product_catalog_initialization(self) -> None:
        """
        Test that ProductCatalog initializes correctly with a strategy.

        Returns:
            None
        """
        catalog = ProductCatalog(sort_by_name)

        assert catalog._sort_strategy is sort_by_name

    # pylint: disable=protected-access
    def test_product_catalog_set_strategy(self) -> None:
        """
        Test that ProductCatalog can change strategies at runtime.

        Returns:
            None
        """
        catalog = ProductCatalog(sort_by_name)
        catalog.set_sort_strategy(sort_by_price_asc)

        assert catalog._sort_strategy is sort_by_price_asc

    @patch("sys.stdout", new_callable=StringIO)
    def test_product_catalog_display_with_name_sort(self, mock_stdout) -> None:
        """
        Test ProductCatalog display method with name sorting strategy.

        Args:
            mock_stdout: Mocked stdout for capturing print output

        Returns:
            None
        """
        catalog = ProductCatalog(sort_by_name)
        catalog.display(self.test_products)

        output = mock_stdout.getvalue()
        lines = output.strip().split("\n")

        assert len(lines) == 3
        assert "Keyboard" in lines[0]
        assert "Monitor" in lines[1]
        assert "Mouse" in lines[2]

    @patch("sys.stdout", new_callable=StringIO)
    def test_product_catalog_display_with_price_sort(self, mock_stdout) -> None:
        """
        Test ProductCatalog display method with price sorting strategy.

        Args:
            mock_stdout: Mocked stdout for capturing print output

        Returns:
            None
        """
        catalog = ProductCatalog(sort_by_price_asc)
        catalog.display(self.test_products)

        output = mock_stdout.getvalue()
        lines = output.strip().split("\n")

        assert len(lines) == 3
        assert "Mouse" in lines[0]
        assert "Keyboard" in lines[1]
        assert "Monitor" in lines[2]


class TestFunctionalStrategyPattern:
    """
    Test cases for the functional Strategy Pattern implementation.
    """

    test_products = [
        {"name": "Zebra", "price": 200.0, "rating": 2.0},
        {"name": "Apple", "price": 100.0, "rating": 5.0},
        {"name": "Beta", "price": 150.0, "rating": 3.0},
    ]

    def test_strategy_pattern_polymorphism(self) -> None:
        """
        Test that different sorting strategies can be used polymorphically.

        Returns:
            None
        """
        strategies = [sort_by_name, sort_by_price_asc, sort_by_price_desc, sort_by_rating]

        results = []
        for strategy in strategies:
            sorted_products = strategy(self.test_products)
            first_product_name = sorted_products[0]["name"]
            results.append(first_product_name)

        # Each strategy should produce a different first item
        expected_first_items = ["Apple", "Apple", "Zebra", "Apple"]  # by name, price asc, price desc, rating
        assert results == expected_first_items

    def test_callable_strategy_interface(self) -> None:
        """
        Test that all sorting strategies are callable with the correct signature.

        Returns:
            None
        """
        strategies = [sort_by_name, sort_by_price_asc, sort_by_price_desc, sort_by_rating]

        for strategy in strategies:
            assert callable(strategy)
            result = strategy(self.test_products)
            assert isinstance(result, list)
            assert len(result) == len(self.test_products)

    def test_strategy_consistency(self) -> None:
        """
        Test that strategies produce consistent results across multiple calls.

        Returns:
            None
        """
        for strategy in [sort_by_name, sort_by_price_asc, sort_by_price_desc, sort_by_rating]:
            result1 = strategy(self.test_products)
            result2 = strategy(self.test_products)

            assert result1 == result2
