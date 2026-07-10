import pytest

from qrp.foundation import QRPError
from qrp.runtime import Container


def test_register_instance() -> None:
    container = Container()
    obj = object()

    container.register_instance("obj", obj)

    assert container.resolve("obj") is obj


def test_duplicate_registration_raises_error() -> None:
    container = Container()

    container.register_instance("obj", object())

    with pytest.raises(QRPError):
        container.register_instance("obj", object())


def test_resolve_unknown_raises_error() -> None:
    container = Container()

    with pytest.raises(QRPError):
        container.resolve("unknown")


def test_contains() -> None:
    container = Container()

    assert container.contains("obj") is False

    container.register_instance("obj", object())

    assert container.contains("obj") is True
