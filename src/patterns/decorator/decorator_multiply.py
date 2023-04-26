"""Decorator example with a parameter."""

from typing import Callable


def multiply_decorator(factor: int) -> Callable[[Callable[[int, int], int]], Callable[[int, int], int]]:
    """
    Decorator that multiplies the decorated function's output by a factor.

    Args:
        factor: Factor to multiply the decorated function's output by.

    Returns:
        The decorated function's output multiplied by a factor.
    """

    def decorator(func: Callable[[int, int], int]) -> Callable[[int, int], int]:
        def wrapper(*args: int) -> int:
            result = func(*args)
            return result * factor

        return wrapper

    return decorator
