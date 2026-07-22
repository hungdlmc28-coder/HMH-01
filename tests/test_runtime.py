"""Tests for the runtime module."""

from qrp.foundation import BaseComponent
from qrp.runtime import ComponentRegistry, Configuration, Runtime


class DummyComponent(BaseComponent):
    """Simple component used for Runtime tests."""

    def __init__(self) -> None:
        super().__init__()


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


def test_runtime_register_component() -> None:
    runtime = Runtime(
        configuration=Configuration(),
        registry=ComponentRegistry(),
    )

    component = DummyComponent()

    runtime.register_component(component)

    assert component.name in runtime.registry.list_components()


def test_runtime_unregister_component() -> None:
    runtime = Runtime(
        configuration=Configuration(),
        registry=ComponentRegistry(),
    )

    component = DummyComponent()

    runtime.register_component(component)
    runtime.unregister_component(component.name)

    assert component.name not in runtime.registry.list_components()


def test_runtime_list_components() -> None:
    runtime = Runtime(
        configuration=Configuration(),
        registry=ComponentRegistry(),
    )

    component = DummyComponent()

    runtime.register_component(component)

    assert runtime.list_components() == [component.name]
