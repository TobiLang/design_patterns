"""Factory module."""
from abc import ABC, abstractmethod

# pylint: disable=too-few-public-methods


class Button(ABC):
    """
    Abstract class representing a Button interface.

    This serves as a base for all specific button implementations. All subclasses
    must implement the `render` method.
    """

    @abstractmethod
    def render(self) -> None:
        """
        Render the button. This method must be implemented by subclasses.
        """


class LightButton(Button):
    """
    Concrete implementation of the Button interface for a light-themed button.
    """

    def render(self) -> None:
        """
        Render a light-themed button.
        """
        print("Rendering a light-themed button.")


class DarkButton(Button):
    """
    Concrete implementation of the Button interface for a dark-themed button.
    """

    def render(self) -> None:
        """
        Render a dark-themed button.
        """
        print("Rendering a dark-themed button.")


class Dialog(ABC):
    """
    Abstract class representing the Dialog creator.

    Contains a factory method `create_button` that must be implemented by
    subclasses to create specific button instances.
    """

    @abstractmethod
    def create_button(self) -> Button:
        """
        Factory method to create a Button instance.

        Returns:
            Button: An instance of a Button.
        """

    def render_window(self) -> None:
        """
        Render the dialog's window and its button.

        Calls the factory method `create_button` to create a button and then renders it.
        """
        button: Button = self.create_button()
        button.render()


class LightThemeDialog(Dialog):
    """
    Concrete implementation of the Dialog class for light-themed dialogs.

    It creates a light-themed button.
    """

    def create_button(self) -> Button:
        """
        Create a light-themed button.

        Returns:
            Button: An instance of LightButton.
        """
        return LightButton()


class DarkThemeDialog(Dialog):
    """
    Concrete implementation of the Dialog class for dark-themed dialogs.

    It creates a dark-themed button.
    """

    def create_button(self) -> Button:
        """
        Create a dark-themed button.

        Returns:
            Button: An instance of DarkButton.
        """
        return DarkButton()


light_dialog: Dialog = LightThemeDialog()
dark_dialog: Dialog = DarkThemeDialog()

light_dialog.render_window()  # Outputs: Rendering a light-themed button.
dark_dialog.render_window()  # Outputs: Rendering a dark-themed button.
