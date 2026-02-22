"""Test prototype module."""

from patterns.prototype.prototype_simple import ConcretePrototype, Prototype


class TestPrototype:
    """Test prototype module."""

    @staticmethod
    def client_code(prototype: Prototype) -> Prototype:
        """
        Mock client code that works with all objects implementing the Prototype interface.

        Args:
            prototype: Prototype object to clone

        Returns:
            Prototype: Cloned object
        """
        return prototype.clone()

    def test_concrete_prototype_clone(self) -> None:
        """
        Test that ConcretePrototype creates proper clones.

        Returns:
            None
        """
        original = ConcretePrototype(42, [1, 2, 3])

        clone = self.client_code(original)

        # Should be different objects
        assert original is not clone

        # Should have same values
        assert original.value == clone.value
        assert original.data == clone.data

    def test_clone_independence(self) -> None:
        """
        Test that cloned objects are independent of the original.

        Returns:
            None
        """
        original = ConcretePrototype(42, [1, 2, 3])
        clone = original.clone()

        # Modify clone
        clone.value = 99
        clone.data.append(4)

        # Original should remain unchanged
        assert original.value == 42
        assert original.data == [1, 2, 3]
        assert clone.value == 99
        assert clone.data == [1, 2, 3, 4]

    def test_deep_copy_behavior(self) -> None:
        """
        Test that clone creates deep copies of nested objects.

        Returns:
            None
        """
        original = ConcretePrototype(10, [{"key": "value"}, [1, 2]])
        clone = original.clone()

        # Modify nested structures in clone
        clone.data[0]["key"] = "modified"
        clone.data[1].append(3)

        # Original nested structures should remain unchanged
        assert original.data[0]["key"] == "value"
        assert original.data[1] == [1, 2]

    def test_repr_method(self) -> None:
        """
        Test the string representation of ConcretePrototype.

        Returns:
            None
        """
        prototype = ConcretePrototype(100, [4, 5, 6])

        expected = "ConcretePrototype(value=100, data=[4, 5, 6])"
        assert repr(prototype) == expected

    def test_multiple_clones(self) -> None:
        """
        Test creating multiple clones from the same original.

        Returns:
            None
        """
        original = ConcretePrototype(7, ["a", "b"])

        clone1 = self.client_code(original)
        clone2 = self.client_code(original)
        clone3 = self.client_code(clone1)

        # All should be different objects
        assert original is not clone1
        assert original is not clone2
        assert clone1 is not clone2
        assert clone1 is not clone3

        # All should have same initial values
        assert original.value == clone1.value == clone2.value == clone3.value
        assert original.data == clone1.data == clone2.data == clone3.data

    def test_empty_data_clone(self) -> None:
        """
        Test cloning with empty data list.

        Returns:
            None
        """
        original = ConcretePrototype(0, [])
        clone = original.clone()

        assert original.data == []
        assert clone.data == []
        assert original.data is not clone.data

    def test_negative_values(self) -> None:
        """
        Test cloning with negative values.

        Returns:
            None
        """
        original = ConcretePrototype(-15, [-1, -2, -3])
        clone = self.client_code(original)

        assert clone.value == -15
        assert clone.data == [-1, -2, -3]
        assert original is not clone
