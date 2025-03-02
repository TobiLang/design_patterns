"""Iterator module."""
from abc import ABC, abstractmethod
from typing import Any, List

# pylint: disable=too-few-public-methods


class IteratorInterface(ABC):
    """
    Defines a custom interface for an iterator.

    Requires the implementation of `has_next()`, `next()`, and `remove()` methods.
    """

    @abstractmethod
    def has_next(self) -> bool:
        """
        Check if there are more elements in the collection.

        Returns:
            bool: True if there are more elements, False otherwise.
        """

    @abstractmethod
    def next(self) -> Any:
        """
        Return the next item in the collection.

        Raises:
            StopIteration: If no more elements are available.

        Return:
            Any: The next item in the collection.
        """

    @abstractmethod
    def remove(self) -> None:
        """
        Remove the last returned item from the collection.

        Raises:
            RuntimeError: If remove is called before next.
        """


class ConcreteIterator(IteratorInterface):
    """
    Concrete implementation of the custom Iterator interface.

    Iterates over a collection of items.
    """

    def __init__(self, collection: List[Any]) -> None:
        """
        Initialize the iterator with a collection.

        Args:
            collection (List[Any]): The collection to iterate over.
        """
        self._collection = collection
        self._index = 0
        self._last_returned_index = -1  # To track the last returned item's index

    def has_next(self) -> bool:
        """
        Check if there are more elements in the collection.

        Returns:
            bool: True if there are more elements, False otherwise.
        """
        return self._index < len(self._collection)

    def next(self) -> Any:
        """
        Return the next item from the collection.

        Returns:
            Any: The next item in the collection.

        Raises:
            StopIteration: If there are no more items in the collection.
        """
        if self.has_next():
            item = self._collection[self._index]
            self._last_returned_index = self._index  # Update the last returned index
            self._index += 1
            return item

        raise StopIteration("No more elements in the collection.")

    def remove(self) -> None:
        """
        Remove the last returned item from the collection.

        Raises:
            RuntimeError: If remove is called before calling next.
        """
        if self._last_returned_index == -1:
            raise RuntimeError("remove() cannot be called before next().")

        # Remove the last returned item
        del self._collection[self._last_returned_index]

        # Adjust the index to account for the removal
        self._index -= 1
        self._last_returned_index = -1  # Reset the last returned index


class IterableInterface(ABC):
    """
    Defines a custom interface for an iterable.

    Requires the implementation of `create_iterator()` method.
    """

    @abstractmethod
    def create_iterator(self) -> IteratorInterface:
        """
        Return an iterator object to allow iteration over the collection.

        Returns:
            IteratorInterface: An iterator for the collection.
        """


# Concrete Iterable
class ConcreteIterable(IterableInterface):
    """
    Concrete implementation of the custom Iterable interface.

    Represents a collection of items that can be iterated over.
    """

    def __init__(self, collection: List[Any]) -> None:
        """
        Initialize the iterable with a collection of items.

        Args:
            collection (List[Any]): The collection of items.
        """
        self._collection = collection

    def create_iterator(self) -> IteratorInterface:
        """
        Return an iterator to iterate over the collection of items.

        Returns:
            IteratorInterface: An iterator for the collection.
        """
        return ConcreteIterator(self._collection)


# Initialize the Iterable
iterable = ConcreteIterable(["Apple", "Banana", "Cherry", "Mango"])

print("Iterating over the objects and removal of an element:")
iterator = iterable.create_iterator()
while iterator.has_next():
    element = iterator.next()
    print(f"  Current element: {element}")
    if element == "Banana":
        iterator.remove()
        print(f"  {element} has been removed!")

print("Iterating over the objects again:")
iterator = iterable.create_iterator()
while iterator.has_next():
    print(f"  Current element: {iterator.next()}")
