"""Tests for the component registry."""

import pytest

from qrp.foundation import BaseComponent, QRPError
from qrp.runtime import ComponentRegistry


class DummyComponent(BaseComponent):
    """Dummy component for testing."""


def test_register_component() -> None:
    registry = ComponentRegistry()
    component = DummyComponent("dummy")

    registry.register(component)

    assert registry.get("dummy") is component


def test_duplicate_registration_raises_error() -> None:
    registry = ComponentRegistry()
    component = DummyComponent("dummy")

    registry.register(component)

    with pytest.raises(QRPError):
        registry.register(component)


def test_unregister_component() -> None:
    registry = ComponentRegistry()
    component = DummyComponent("dummy")

    registry.register(component)
    registry.unregister("dummy")

    assert registry.get("dummy") is None


def test_list_components() -> None:
    registry = ComponentRegistry()

    registry.register(DummyComponent("b"))
    registry.register(DummyComponent("a"))

    assert registry.list_components() == ["a", "b"]


def test_register_invalid_component() -> None:
    registry = ComponentRegistry()

    with pytest.raises(TypeError):
        registry.register(object())  # type: ignore[arg-type]
