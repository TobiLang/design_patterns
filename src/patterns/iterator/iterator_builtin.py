"""Iterator module."""
from typing import Any, Iterable, Iterator, List

# pylint: disable=too-few-public-methods


class ConcreteIterable(Iterable):
    """
    A simplified Iterable class that supports iteration and element removal.

    The example is using Python's built-in iterator protocol.
    """

    def __init__(self, collection: List[Any]) -> None:
        """
        Initialize the iterable with a collection of items.

        Args:
            collection (list): The collection to iterate over.
        """
        self._collection = collection

    def __iter__(self) -> Iterator:
        """
        Return an iterator object for the collection.

        Returns:
            ConcreteIterator: An iterator for the collection.
        """
        return ConcreteIterator(self._collection)


class ConcreteIterator(Iterator):
    """
    A concrete implementation of an iterator using Python's built-in methods.

    Supports iteration and element removal.
    """

    def __init__(self, collection):
        """
        Initialize the iterator with a collection.

        Args:
            collection (list): The collection to iterate over.
        """
        self._collection = collection
        self._index = 0

    def __iter__(self) -> Iterator:
        """
        Return self as the iterator object.

        Returns:
            self
        """
        return self

    def __next__(self) -> Any:
        """
        Return the next item in the collection.

        Returns:
            Any: The next item in the collection.

        Raises:
            StopIteration: If there are no more items to iterate.
        """
        if self._index < len(self._collection):
            item = self._collection[self._index]
            self._index += 1
            return item
        raise StopIteration


# Example usage
iterable = ConcreteIterable(["Apple", "Banana", "Cherry", "Mango"])

print("Iterating over the objects:")
for element in iter(iterable):
    print(f"  Current element: {element}")

print("Iterating over the objects without explicitly using iter:")
for element in iterable:
    print(f"  Current element: {element}")
