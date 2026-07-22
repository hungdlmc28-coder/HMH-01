"""Tests for the runtime module."""

import pytest

from qrp.foundation import BaseComponent
from qrp.runtime import (
    ComponentRegistry,
    Configuration,
    LifecycleError,
    LifecycleState,
    Runtime,
)


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


def test_runtime_registers_component_with_lifecycle() -> None:
    runtime = Runtime(
        configuration=Configuration(),
        registry=ComponentRegistry(),
    )

    component = DummyComponent()

    runtime.register_component(component)

    assert runtime.lifecycle_state(component) is LifecycleState.CREATED


def test_runtime_initializes_registered_components() -> None:
    runtime = Runtime(
        configuration=Configuration(),
        registry=ComponentRegistry(),
    )

    component = DummyComponent()

    runtime.register_component(component)
    runtime.initialize_components()

    assert runtime.lifecycle_state(component) is LifecycleState.INITIALIZED


def test_runtime_starts_initialized_components() -> None:
    runtime = Runtime(
        configuration=Configuration(),
        registry=ComponentRegistry(),
    )

    component = DummyComponent()

    runtime.register_component(component)
    runtime.initialize_components()
    runtime.start_components()

    assert runtime.lifecycle_state(component) is LifecycleState.RUNNING


def test_runtime_stops_running_components() -> None:
    runtime = Runtime(
        configuration=Configuration(),
        registry=ComponentRegistry(),
    )

    component = DummyComponent()

    runtime.register_component(component)
    runtime.initialize_components()
    runtime.start_components()
    runtime.stop_components()

    assert runtime.lifecycle_state(component) is LifecycleState.STOPPED


def test_runtime_unregisters_stopped_component() -> None:
    runtime = Runtime(
        configuration=Configuration(),
        registry=ComponentRegistry(),
    )

    component = DummyComponent()

    runtime.register_component(component)
    runtime.initialize_components()
    runtime.start_components()
    runtime.stop_components()
    runtime.unregister_component(component.name)

    assert component.name not in runtime.list_components()


def test_runtime_unregisters_component_from_lifecycle() -> None:
    runtime = Runtime(
        configuration=Configuration(),
        registry=ComponentRegistry(),
    )

    component = DummyComponent()

    runtime.register_component(component)
    runtime.unregister_component(component.name)

    with pytest.raises(LifecycleError):
        runtime.lifecycle_state(component)
