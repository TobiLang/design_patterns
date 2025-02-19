"""Flyweight module."""

from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

# pylint: disable=too-few-public-methods


class CharacterFlyweight(ABC):
    """Abstract class representing a character."""

    @abstractmethod
    def display(self, font: str) -> None:
        """
        Display character with a specific font.

        Returns:
            None
        """


class ConcreteCharacter(CharacterFlyweight):
    """Representing a concrete character to use."""

    def __init__(self, char: str) -> None:
        """
        Initialize the class with a character.
        """
        self.char = char

    def display(self, font: str) -> None:
        """
        Display character with a specific font.

        Returns:
            None
        """
        print(f"Character '{self.char}' displayed in font: {font}")


class CharacterFactory:
    """Flyweight Factory: Manages shared character instances."""

    characters: Dict[str, CharacterFlyweight] = {}

    @classmethod
    def get_character(cls, char: str) -> CharacterFlyweight:
        """
        Return an existing flyweight or create a new one.

        Returns:
            CharacterFlyweight: share instance
        """
        if char not in cls.characters:
            cls.characters[char] = ConcreteCharacter(char)
        return cls.characters[char]


class TextEditorClient:
    """A simple text editor making use of flyweights to reduce memory usage."""

    def __init__(self) -> None:
        """
        Character list holding the actual text and a font for each character.
        """
        self.characters: List[Tuple[CharacterFlyweight, str]] = []

    def add_character(self, char: str, font: str) -> None:
        """
        Add a new character to the text and set its font.

        Args:
            *char: Char to add
            **font: Font to use for the character

        Returns:
            None
        """
        flyweight = CharacterFactory.get_character(char)
        self.characters.append((flyweight, font))

    def render(self) -> None:
        """
        Display all characters with their respective fonts.

        Returns:
            None
        """
        for flyweight, font in self.characters:
            flyweight.display(font)


# Example Usage
editor = TextEditorClient()
editor.add_character("H", "Arial")
editor.add_character("e", "Arial")
editor.add_character("l", "Arial")
editor.add_character("l", "Arial")
editor.add_character("o", "Times New Roman")
editor.add_character("!", "Times New Roman")

print("Rendering Text:")
editor.render()

print("Size of the characters list: ", len(editor.characters))
print("Size of the flyweight dictionary: ", len(CharacterFactory.characters))

# Output
# Rendering Text:
# Character 'H' displayed in font: Arial
# Character 'e' displayed in font: Arial
# Character 'l' displayed in font: Arial
# Character 'l' displayed in font: Arial
# Character 'o' displayed in font: Times New Roman
# Character '!' displayed in font: Times New Roman
#
# Size of the characters list:  6
# Size of the flyweight dictionary:  5
