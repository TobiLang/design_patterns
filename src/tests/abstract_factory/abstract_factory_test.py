"""Unit tests for abstract_factory module."""

from patterns.abstract_factory.abstract_factory import (
    DarkButton,
    DarkCheckbox,
    DarkTextField,
    DarkThemeFactory,
    LightButton,
    LightCheckbox,
    LightTextField,
    LightThemeFactory,
    build_login_form,
)


class TestAbstractFactory:
    """Test cases for the Abstract Factory pattern implementation."""

    @staticmethod
    def test_light_theme_factory_creates_correct_components():
        """Test that LightThemeFactory creates light theme components."""
        light_factory = LightThemeFactory()

        button = light_factory.create_button()
        text_field = light_factory.create_text_field()
        checkbox = light_factory.create_checkbox()

        assert isinstance(button, LightButton)
        assert isinstance(text_field, LightTextField)
        assert isinstance(checkbox, LightCheckbox)

    @staticmethod
    def test_dark_theme_factory_creates_correct_components():
        """Test that DarkThemeFactory creates dark theme components."""
        dark_factory = DarkThemeFactory()

        button = dark_factory.create_button()
        text_field = dark_factory.create_text_field()
        checkbox = dark_factory.create_checkbox()

        assert isinstance(button, DarkButton)
        assert isinstance(text_field, DarkTextField)
        assert isinstance(checkbox, DarkCheckbox)

    @staticmethod
    def test_light_components_render_correctly():
        """Test that light theme components render with correct content."""
        light_factory = LightThemeFactory()

        button = light_factory.create_button()
        text_field = light_factory.create_text_field()
        checkbox = light_factory.create_checkbox()

        assert "white background" in button.render()
        assert "light gray input" in text_field.render()
        assert "white fill" in checkbox.render()

    @staticmethod
    def test_dark_components_render_correctly():
        """Test that dark theme components render with correct content."""
        dark_factory = DarkThemeFactory()

        button = dark_factory.create_button()
        text_field = dark_factory.create_text_field()
        checkbox = dark_factory.create_checkbox()

        assert "dark gray background" in button.render()
        assert "charcoal input" in text_field.render()
        assert "dark fill" in checkbox.render()

    @staticmethod
    def test_build_login_form_with_light_theme():
        """Test the build_login_form function with the light theme factory."""
        light_factory = DarkThemeFactory()
        build_login_form(light_factory)

    @staticmethod
    def test_build_login_form_with_dark_theme():
        """Test the build_login_form function with the dark theme factory."""
        dark_factory = DarkThemeFactory()
        build_login_form(dark_factory)
