"""Tests for the configuration system."""

from qrp.runtime import Configuration


def test_set_and_get_value() -> None:
    config = Configuration()

    config.set("runtime.debug", True)

    assert config.get("runtime.debug") is True


def test_get_default_value() -> None:
    config = Configuration()

    assert config.get("missing", default=42) == 42


def test_has_key() -> None:
    config = Configuration()

    config.set("runtime.name", "qrp")

    assert config.has("runtime.name")
    assert not config.has("runtime.version")


def test_remove_key() -> None:
    config = Configuration()

    config.set("runtime.debug", True)
    config.remove("runtime.debug")

    assert not config.has("runtime.debug")


def test_clear_configuration() -> None:
    config = Configuration()

    config.set("a", 1)
    config.set("b", 2)

    config.clear()

    assert not config.has("a")
    assert not config.has("b")
