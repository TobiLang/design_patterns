"""Test composite module."""

import sys
from io import StringIO

import pytest

from patterns.composite.composite import Composite, Leaf, client_code


class TestComposite:
    """Test composite pattern implementation."""

    def test_leaf_operation(self) -> None:
        """Test that a leaf returns correct operation result."""
        leaf = Leaf("TestLeaf")
        assert leaf.operation() == "Leaf(TestLeaf)"

    def test_leaf_add_raises_error(self) -> None:
        """Test that adding to a leaf raises NotImplementedError."""
        leaf = Leaf("TestLeaf")
        another_leaf = Leaf("AnotherLeaf")

        with pytest.raises(NotImplementedError, match="Leaf does not support add"):
            leaf.add(another_leaf)

    def test_leaf_remove_raises_error(self) -> None:
        """Test that removing from a leaf raises NotImplementedError."""
        leaf = Leaf("TestLeaf")
        another_leaf = Leaf("AnotherLeaf")

        with pytest.raises(NotImplementedError, match="Leaf does not support remove"):
            leaf.remove(another_leaf)

    def test_leaf_get_children_empty(self) -> None:
        """Test that a leaf returns empty children list."""
        leaf = Leaf("TestLeaf")
        assert not leaf.get_children()

    def test_composite_empty_operation(self) -> None:
        """Test that an empty composite returns correct operation result."""
        composite = Composite("EmptyBranch")
        assert composite.operation() == "Branch(EmptyBranch)[]"

    def test_composite_with_single_leaf(self) -> None:
        """Test composite with a single leaf component."""
        composite = Composite("Branch")
        leaf = Leaf("A")
        composite.add(leaf)

        assert composite.operation() == "Branch(Branch)[Leaf(A)]"

    def test_composite_with_multiple_leaves(self) -> None:
        """Test composite with multiple leaf components."""
        composite = Composite("Branch")
        composite.add(Leaf("A"))
        composite.add(Leaf("B"))
        composite.add(Leaf("C"))

        assert composite.operation() == "Branch(Branch)[Leaf(A), Leaf(B), Leaf(C)]"

    def test_composite_nested_structure(self) -> None:
        """Test nested composite structure."""
        root = Composite("Root")
        root.add(Leaf("A"))
        root.add(Leaf("B"))

        sub_branch = Composite("Sub")
        sub_branch.add(Leaf("C"))
        sub_branch.add(Leaf("D"))
        root.add(sub_branch)

        expected = "Branch(Root)[Leaf(A), Leaf(B), Branch(Sub)[Leaf(C), Leaf(D)]]"
        assert root.operation() == expected

    def test_composite_remove_component(self) -> None:
        """Test removing a component from composite."""
        composite = Composite("Branch")
        leaf_a = Leaf("A")
        leaf_b = Leaf("B")

        composite.add(leaf_a)
        composite.add(leaf_b)
        assert composite.operation() == "Branch(Branch)[Leaf(A), Leaf(B)]"

        composite.remove(leaf_a)
        assert composite.operation() == "Branch(Branch)[Leaf(B)]"

    def test_composite_get_children(self) -> None:
        """Test getting children from composite."""
        composite = Composite("Branch")
        leaf_a = Leaf("A")
        leaf_b = Leaf("B")

        composite.add(leaf_a)
        composite.add(leaf_b)

        children = composite.get_children()
        assert len(children) == 2
        assert leaf_a in children
        assert leaf_b in children

    def test_client_code_with_leaf(self) -> None:
        """Test client code with a leaf component."""
        leaf = Leaf("TestLeaf")

        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        client_code(leaf)

        # Restore stdout
        sys.stdout = sys.__stdout__

        assert captured_output.getvalue().strip() == "Leaf(TestLeaf)"

    def test_client_code_with_composite(self) -> None:
        """Test client code with a composite component."""
        composite = Composite("TestBranch")
        composite.add(Leaf("A"))
        composite.add(Leaf("B"))

        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        client_code(composite)

        # Restore stdout
        sys.stdout = sys.__stdout__

        assert captured_output.getvalue().strip() == "Branch(TestBranch)[Leaf(A), Leaf(B)]"

    def test_deep_nesting(self) -> None:
        """Test deeply nested composite structure."""
        level1 = Composite("Level1")
        level2 = Composite("Level2")
        level3 = Composite("Level3")

        level3.add(Leaf("Deep"))
        level2.add(level3)
        level2.add(Leaf("Middle"))
        level1.add(level2)
        level1.add(Leaf("Top"))

        expected = "Branch(Level1)[Branch(Level2)[Branch(Level3)[Leaf(Deep)], Leaf(Middle)], Leaf(Top)]"
        assert level1.operation() == expected
