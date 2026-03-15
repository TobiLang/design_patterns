"""Functional strategy module."""

from typing import Callable, List


# Strategies as simple functions
def sort_by_name(items: List[dict]) -> List[dict]:
    """Sort items by name."""
    return sorted(items, key=lambda x: x["name"])


def sort_by_price_asc(items: List[dict]) -> List[dict]:
    """Sort items by price in ascending order."""
    return sorted(items, key=lambda x: x["price"])


def sort_by_price_desc(items: List[dict]) -> List[dict]:
    """Sort items by price in descending order."""
    return sorted(items, key=lambda x: x["price"], reverse=True)


def sort_by_rating(items: List[dict]) -> List[dict]:
    """Sort items by rating in descending order."""
    return sorted(items, key=lambda x: x["rating"], reverse=True)


# Context using a callable strategy
class ProductCatalog:
    """Product catalog class that supports sorting products."""

    def __init__(self, sort_strategy: Callable[[List[dict]], List[dict]]) -> None:
        """Initialize the catalog with a sorting strategy."""
        self._sort_strategy = sort_strategy

    def set_sort_strategy(self, strategy: Callable[[List[dict]], List[dict]]) -> None:
        """Set the sorting strategy for the catalog."""
        self._sort_strategy = strategy

    def display(self, products: List[dict]) -> None:
        """Display the products in the catalog."""
        for product in self._sort_strategy(products):
            print(f"  {product['name']:<15} ${product['price']:>6.2f}  Stars: {product['rating']}")


# Usage example
sample_products = [
    {"name": "Keyboard", "price": 89.99, "rating": 4.5},
    {"name": "Mouse", "price": 49.99, "rating": 4.8},
    {"name": "Monitor", "price": 349.99, "rating": 4.2},
    {"name": "Headset", "price": 129.99, "rating": 4.6},
]

catalog = ProductCatalog(sort_by_price_asc)
print("By price (low to high):")
catalog.display(sample_products)
catalog.set_sort_strategy(sort_by_rating)
print("\nBy rating:")
catalog.display(sample_products)

# Output:
# By price (low to high):
#   Mouse           $ 49.99  Stars: 4.8
#   Keyboard        $ 89.99  Stars: 4.5
#   Headset         $129.99  Stars: 4.6
#   Monitor         $349.99  Stars: 4.2
#
# By rating:
#   Mouse           $ 49.99  Stars: 4.8
#   Headset         $129.99  Stars: 4.6
#   Keyboard        $ 89.99  Stars: 4.5
#   Monitor         $349.99  Stars: 4.2
