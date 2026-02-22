"""Class realizing the simple Prototype design pattern."""

import copy
from abc import ABC, abstractmethod


# pylint: disable=too-few-public-methods
class Prototype(ABC):
    """
    Abstract class defining the prototype interface.
    """

    @abstractmethod
    def clone(self) -> "Prototype":
        """
        Create a copy of the current object.

        Returns:
            Prototype: A new instance that is a copy of the current object.
        """


class ConcretePrototype(Prototype):
    """
    Concrete implementation of the Prototype pattern.
    """

    def __init__(self, value: int, data: list) -> None:
        """
        Initialize a ConcretePrototype instance.

        Args:
            value (int): An integer value to store.
            data (List[Any]): A list of data elements.
        """
        self.value = value
        self.data = data

    def clone(self) -> "ConcretePrototype":
        """
        Create a deep copy of the current ConcretePrototype instance.

        Returns:
            ConcretePrototype: A new ConcretePrototype instance that is
                              a deep copy of the current instance.
        """

        return copy.deepcopy(self)

    def __repr__(self) -> str:
        """
        Return a string representation of the ConcretePrototype instance.

        Returns:
            str: A string representation showing the value and data attributes.
        """

        return f"ConcretePrototype(value={self.value}, data={self.data})"


# Client code
original = ConcretePrototype(42, [1, 2, 3])
clone = original.clone()
clone.value = 99
clone.data.append(4)
print(original)
print(clone)
