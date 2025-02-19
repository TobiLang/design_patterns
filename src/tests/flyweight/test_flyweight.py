"""Test flyweight module."""

import sys
from io import StringIO

from patterns.flyweight.flyweight import CharacterFactory, TextEditorClient


class TestFlyweightPattern:
    """
    Test cases for the implementation of the Flyweight Pattern.
    """

    def test_character_factory_creates_only_one_instance_for_char(self) -> None:
        """
        Test that the CharacterFactory reuses instances for the same character.

        Returns:
            None
        """
        char_a1 = CharacterFactory.get_character("A")
        char_a2 = CharacterFactory.get_character("A")

        assert char_a1 is char_a2

    def test_character_factory_creates_new_instance_for_different_chars(self) -> None:
        """
        Test that the CharacterFactory creates new instances for different characters.

        Returns:
            None
        """

        char_a = CharacterFactory.get_character("A")
        char_b = CharacterFactory.get_character("B")

        assert char_a is not char_b
        assert char_a.char == "A"
        assert char_b.char == "B"

    def test_add_character_to_text_editor(self) -> None:
        """
        Test adding characters to the text editor and using the correct flyweights.

        Returns:
            None
        """
        editor = TextEditorClient()
        editor.add_character("A", "Arial")
        editor.add_character("B", "Times New Roman")
        editor.add_character("A", "Verdana")

        # Ensure that the editor stores the characters with respective fonts
        assert len(editor.characters) == 3
        assert editor.characters[0][1] == "Arial"
        assert editor.characters[2][1] == "Verdana"
        assert editor.characters[0][0] == editor.characters[2][0]

    def test_exact_render_output(self) -> None:
        """
        Test the rendering of characters and ensure correct output.

        Returns:
            None
        """
        editor = TextEditorClient()
        editor.add_character("A", "Arial")
        editor.add_character("B", "Times New Roman")
        editor.add_character("A", "Verdana")

        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        editor.render()

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Verify the captured output matches expectations
        expected_output = (
            "Character 'A' displayed in font: Arial\n"
            "Character 'B' displayed in font: Times New Roman\n"
            "Character 'A' displayed in font: Verdana\n"
        )
        assert captured_output.getvalue() == expected_output
