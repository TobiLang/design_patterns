"""Test Iterator module."""

import pytest

from patterns.iterator.iterator_builtin import ConcreteIterable, ConcreteIterator


class TestConcreteIterator:
    """Unit tests for the ConcreteIterator class."""

    def test_iterator_iteration(self) -> None:
        """Test iteration functionality of the ConcreteIterator."""
        collection = ["Apple", "Banana", "Cherry"]
        iterator = ConcreteIterator(collection)

        # Test __next__ functionality
        assert next(iterator) == "Apple"
        assert next(iterator) == "Banana"
        assert next(iterator) == "Cherry"

        # Once the iterator is exhausted, StopIteration should be raised
        with pytest.raises(StopIteration):
            next(iterator)

    def test_iterator_reusability(self) -> None:
        """Ensure the iterator is not reusable after being exhausted."""
        collection = ["Apple", "Banana", "Cherry"]
        iterator = ConcreteIterator(collection)

        # Exhaust the iterator
        for _ in collection:
            next(iterator)

        # Further calls should raise StopIteration
        with pytest.raises(StopIteration):
            next(iterator)

    def test_empty_iterator(self) -> None:
        """Test behavior when the iterator is initialized with an empty collection."""
        collection = []
        iterator = ConcreteIterator(collection)

        # Should immediately raise StopIteration
        with pytest.raises(StopIteration):
            next(iterator)


class TestConcreteIterable:
    """Unit tests for the ConcreteIterable class."""

    def test_iteration(self) -> None:
        """Test the iteration functionality of ConcreteIterable."""
        collection = ["Apple", "Banana", "Cherry"]
        iterable = ConcreteIterable(collection)

        # Use the iterable in a for loop
        elements = [iter(iterable)]

        # Ensure that the elements match the expected collection
        assert elements == collection

    def test_multiple_iterations(self) -> None:
        """Test that the iterable can be iterated multiple times."""
        collection = ["Apple", "Banana", "Cherry"]
        iterable = ConcreteIterable(collection)

        # First iteration
        first_iteration = [iter(iterable)]
        # Second iteration
        second_iteration = [iter(iterable)]

        # Both iterations should yield the same elements
        assert first_iteration == collection
        assert second_iteration == collection

    def test_empty_iterable(self) -> None:
        """Test behavior when the iterable is initialized with an empty collection."""
        collection = []
        iterable = ConcreteIterable(collection)

        # Iterating over an empty iterable should produce no elements
        elements = [iter(iterable)]
        assert not elements
