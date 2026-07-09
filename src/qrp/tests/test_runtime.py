"""Tests for the runtime module."""

from qrp.runtime import Runtime


def test_runtime_initial_state() -> None:
    runtime = Runtime()

    assert runtime.is_running is False
    assert runtime.is_initialized is False


def test_runtime_start() -> None:
    runtime = Runtime()

    runtime.start()

    assert runtime.is_running is True
    assert runtime.is_initialized is True


def test_runtime_stop() -> None:
    runtime = Runtime()

    runtime.start()
    runtime.stop()

    assert runtime.is_running is False
    assert runtime.is_initialized is False
