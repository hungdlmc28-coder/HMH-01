"""Tests for Bootstrap."""

from qrp.runtime import Bootstrap, Configuration


def test_bootstrap_build_runtime() -> None:
    bootstrap = Bootstrap()
    runtime = bootstrap.build()

    assert runtime is not None


def test_bootstrap_creates_configuration() -> None:
    runtime = Bootstrap().build()

    assert runtime.configuration is not None


def test_bootstrap_creates_registry() -> None:
    runtime = Bootstrap().build()

    assert runtime.registry is not None


def test_bootstrap_uses_supplied_configuration() -> None:
    config = Configuration()
    config.set("runtime.debug", True)

    runtime = Bootstrap().build(config=config)

    assert runtime.configuration.get("runtime.debug") is True
