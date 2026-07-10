"""Tests for the runtime module."""

from qrp.runtime import ComponentRegistry, Configuration, Runtime


def test_runtime_initial_state() -> None:
    runtime = Runtime(
        configuration=Configuration(),
        registry=ComponentRegistry(),
    )

    assert runtime.is_running is False
    assert runtime.is_initialized is False


def test_runtime_start() -> None:
    runtime = Runtime(
        configuration=Configuration(),
        registry=ComponentRegistry(),
    )

    runtime.start()

    assert runtime.is_running is True
    assert runtime.is_initialized is True


def test_runtime_stop() -> None:
    runtime = Runtime(
        configuration=Configuration(),
        registry=ComponentRegistry(),
    )

    runtime.start()
    runtime.stop()

    assert runtime.is_running is False
    assert runtime.is_initialized is False
