"""Demonstrating the difference of shallow vs. deep copy behavior in Python."""

import copy


# pylint: disable=too-few-public-methods
class Address:
    """Represents a physical address."""

    def __init__(self, city: str):
        """
        Initialize an Address instance.

        Args:
            city (str): The name of the city for this address.
        """
        self.city = city

    def __repr__(self):
        """Return a string representation of the Address."""
        return f"'{self.city}')"


# pylint: disable=too-few-public-methods
class Person:
    """Represents a person with a name and address."""

    def __init__(self, name: str, address: Address):
        """
        Initialize a Person instance.

        Args:
            name (str): The person's name.
            address (Address): The person's address object.
        """
        self.name = name
        self.address = address

    def __repr__(self):
        """Return a string representation of the Person."""
        return f"Person('{self.name}', {self.address})"


original = Person("Alice", Address("Berlin"))
shallow = copy.copy(original)
deep = copy.deepcopy(original)

# Modifying the address through the shallow copy affects the original
shallow.address.city = "Munich"
print(f"Orig: {original} - Shallow: {shallow} - Deep {deep}")

# Modifying the address through the deep copy does NOT affect the original
deep.address.city = "Hamburg"
print(f"Orig: {original} - Shallow: {shallow} - Deep {deep}")
