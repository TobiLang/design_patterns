"""Test Iterator module."""

import pytest

from patterns.iterator.iterator import ConcreteIterable, ConcreteIterator


class TestConcreteIterator:
    """Unit tests for ConcreteIterator."""

    def test_next_and_has_next(self) -> None:
        """Test the `next()` and `has_next()` methods."""
        collection = ["Apple", "Banana", "Cherry"]
        iterator = ConcreteIterator(collection)

        # Check that has_next() returns True initially
        assert iterator.has_next()

        # Retrieve and validate items using next()
        assert iterator.next() == "Apple"
        assert iterator.next() == "Banana"
        assert iterator.next() == "Cherry"

        # No more elements; has_next() should return False
        assert not iterator.has_next()

        # Calling next() should raise StopIteration
        with pytest.raises(StopIteration):
            iterator.next()

    def test_remove(self) -> None:
        """Test the ability to remove an item using `remove()`."""
        collection = ["Apple", "Banana", "Cherry"]
        iterator = ConcreteIterator(collection)

        # Move to the second element
        iterator.next()
        iterator.next()

        # Remove the second element ("Banana")
        iterator.remove()

        # Validate that the element has been removed from the collection
        assert collection == ["Apple", "Cherry"]

        # Ensure the iterator works correctly after removal
        assert iterator.next() == "Cherry"

    def test_remove_without_next(self) -> None:
        """Test that calling `remove()` before `next()` raises RuntimeError."""
        collection = ["Apple", "Banana", "Cherry"]
        iterator = ConcreteIterator(collection)

        with pytest.raises(RuntimeError, match="remove\\(\\) cannot be called before next\\(\\)."):
            iterator.remove()


class TestConcreteIterable:
    """Unit tests for ConcreteIterable."""

    def test_create_iterator(self) -> None:
        """Ensure that the iterable creates an iterator successfully."""
        collection = ["Apple", "Banana", "Cherry"]
        iterable = ConcreteIterable(collection)
        iterator = iterable.create_iterator()

        # Check that an iterator is created
        assert isinstance(iterator, ConcreteIterator)

        # Validate that the iterator works correctly
        assert iterator.next() == "Apple"
        assert iterator.has_next()

    def test_combined_usage(self) -> None:
        """Test combined usage of iterable and iterator for removing an element."""
        collection = ["Apple", "Banana", "Cherry", "Mango"]
        iterable = ConcreteIterable(collection)
        iterator = iterable.create_iterator()

        # Iterate and remove "Banana"
        removed_element = None
        while iterator.has_next():
            element = iterator.next()
            if element == "Banana":
                iterator.remove()
                removed_element = element

        # Ensure "Banana" was removed
        assert removed_element == "Banana"
        assert collection == ["Apple", "Cherry", "Mango"]

        # Reiterate through the modified collection
        iterator = iterable.create_iterator()
        elements = []
        while iterator.has_next():
            elements.append(iterator.next())

        # Verify the remaining collection
        assert elements == ["Apple", "Cherry", "Mango"]

        # Ensure StopIteration is raised for exhausted iterator
        with pytest.raises(StopIteration):
            iterator.next()
