"""Conftest for Proxy Pattern."""
import pytest

from patterns.proxy.proxy import RealSubject


@pytest.fixture
def real_subject() -> RealSubject:
    """
    RealSubject.

    Returns:
        RealSubject
    """
    return RealSubject()
