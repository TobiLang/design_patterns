"""Test factory module."""
import unittest
from unittest.mock import patch

from patterns.factory.dialog_factory import (
    Button,
    DarkButton,
    DarkThemeDialog,
    Dialog,
    LightButton,
    LightThemeDialog,
)


class TestButtonImplementations(unittest.TestCase):
    """
    Test cases for the implementations of the Button interface.
    """

    def test_light_button_render(self):
        """
        Ensure the LightButton render method outputs the correct text.
        """
        light_button: Button = LightButton()
        with patch("builtins.print") as mocked_print:
            light_button.render()
            mocked_print.assert_called_once_with("Rendering a light-themed button.")

    def test_dark_button_render(self):
        """
        Ensure the DarkButton render method outputs the correct text.
        """
        dark_button: Button = DarkButton()
        with patch("builtins.print") as mocked_print:
            dark_button.render()
            mocked_print.assert_called_once_with("Rendering a dark-themed button.")


class TestDialogImplementations(unittest.TestCase):
    """
    Test cases for the concrete Dialog classes and their factory methods.
    """

    def test_light_theme_dialog_creates_light_button(self):
        """
        Ensure LightThemeDialog creates a LightButton instance.
        """
        dialog: Dialog = LightThemeDialog()
        button = dialog.create_button()
        self.assertIsInstance(button, LightButton, "Factory method should return a LightButton instance.")

    def test_dark_theme_dialog_creates_dark_button(self):
        """
        Ensure DarkThemeDialog creates a DarkButton instance.
        """
        dialog: Dialog = DarkThemeDialog()
        button = dialog.create_button()
        self.assertIsInstance(button, DarkButton, "Factory method should return a DarkButton instance.")

    def test_light_theme_dialog_render_window(self):
        """
        Test the render_window method of LightThemeDialog.
        It should call the render method of LightButton.
        """
        dialog: Dialog = LightThemeDialog()
        with patch("builtins.print") as mocked_print:
            dialog.render_window()
            mocked_print.assert_called_once_with("Rendering a light-themed button.")

    def test_dark_theme_dialog_render_window(self):
        """
        Test the render_window method of DarkThemeDialog.
        It should call the render method of DarkButton.
        """
        dialog: Dialog = DarkThemeDialog()
        with patch("builtins.print") as mocked_print:
            dialog.render_window()
            mocked_print.assert_called_once_with("Rendering a dark-themed button.")


if __name__ == "__main__":
    unittest.main()
