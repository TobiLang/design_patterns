"""Abstract Factory module."""

from abc import ABC, abstractmethod

# pylint: disable=too-few-public-methods


class Button(ABC):
    """Abstract base class for button components."""

    @abstractmethod
    def render(self) -> str:
        """Render the button component."""


class TextField(ABC):
    """Abstract base class for textfield components."""

    @abstractmethod
    def render(self) -> str:
        """Render the textfield component."""


class Checkbox(ABC):
    """Render the checkbox component."""

    @abstractmethod
    def render(self) -> str:
        """Render the checkbox component."""


class LightButton(Button):
    """Light theme implementation of a button component."""

    def render(self) -> str:
        """Render the light theme button."""
        return "Button: [white background, dark text, subtle shadow]"


class LightTextField(TextField):
    """Light theme implementation of a textfield component."""

    def render(self) -> str:
        """Render the light theme textfield."""
        return "TextField: [light gray input, dark placeholder, thin border]"


class LightCheckbox(Checkbox):
    """Light theme implementation of a checkbox component."""

    def render(self) -> str:
        """Render the light theme checkbox."""
        return "Checkbox: [white fill, dark checkmark, gray border]"


class DarkButton(Button):
    """Dark theme implementation of a button component."""

    def render(self) -> str:
        """Render the Dark theme button."""
        return "Button: [dark gray background, white text, neon accent]"


class DarkTextField(TextField):
    """Dark theme implementation of a textfield component."""

    def render(self) -> str:
        """Render the Dark theme textfield."""
        return "TextField: [charcoal input, light placeholder, bright border]"


class DarkCheckbox(Checkbox):
    """Dark theme implementation of a checkbox component."""

    def render(self) -> str:
        """Render the Dark theme checkbox."""
        return "Checkbox: [dark fill, bright checkmark, subtle border]"


class UIFactory(ABC):
    """Abstract factory for creating UI components."""

    @abstractmethod
    def create_button(self) -> Button:
        """Create a button component."""

    @abstractmethod
    def create_text_field(self) -> TextField:
        """Create a textfield component."""

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        """Create a checkbox component."""


class LightThemeFactory(UIFactory):
    """Factory for creating light-themed UI components."""

    def create_button(self) -> Button:
        """Create a light theme button."""
        return LightButton()

    def create_text_field(self) -> TextField:
        """Create a light theme textfield."""
        return LightTextField()

    def create_checkbox(self) -> Checkbox:
        """Create a light theme checkbox."""
        return LightCheckbox()


class DarkThemeFactory(UIFactory):
    """Factory for creating dark-themed UI components."""

    def create_button(self) -> Button:
        """Create a dark theme button."""
        return DarkButton()

    def create_text_field(self) -> TextField:
        """Create a dark theme textfield."""
        return DarkTextField()

    def create_checkbox(self) -> Checkbox:
        """Create a dark theme checkbox."""
        return DarkCheckbox()


def build_login_form(factory: UIFactory) -> None:
    """Build and display a login form using the given UI factory."""
    button = factory.create_button()
    text_field = factory.create_text_field()
    checkbox = factory.create_checkbox()
    print("Login Form:")
    print(f"  Username: {text_field.render()}")
    print(f"  Submit:   {button.render()}")
    print(f"  Remember: {checkbox.render()}")
