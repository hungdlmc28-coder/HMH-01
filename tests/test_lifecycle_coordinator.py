import pytest

from qrp.runtime import (
    LifecycleCoordinator,
    LifecycleError,
    LifecycleState,
)


class DummyComponent:
    """Simple component used for LifecycleCoordinator tests."""


def test_register_component() -> None:
    # Arrange
    coordinator = LifecycleCoordinator()
    component = DummyComponent()

    # Act
    coordinator.register(component)

    # Assert
    assert coordinator.state(component) is LifecycleState.CREATED


def test_state_returns_created_after_registration() -> None:
    # Arrange
    coordinator = LifecycleCoordinator()
    component = DummyComponent()

    coordinator.register(component)

    # Act
    state = coordinator.state(component)

    # Assert
    assert state is LifecycleState.CREATED


def test_state_unknown_component_raises_error() -> None:
    # Arrange
    coordinator = LifecycleCoordinator()
    component = DummyComponent()

    # Act / Assert
    with pytest.raises(LifecycleError):
        coordinator.state(component)


def test_duplicate_registration_raises_error() -> None:
    # Arrange
    coordinator = LifecycleCoordinator()
    component = DummyComponent()

    coordinator.register(component)

    # Act / Assert
    with pytest.raises(LifecycleError):
        coordinator.register(component)


def test_start_transitions_initialized_to_running() -> None:
    # Arrange
    coordinator = LifecycleCoordinator()
    component = DummyComponent()

    coordinator.register(component)
    coordinator.initialize()

    # Act
    coordinator.start()

    # Assert
    assert coordinator.state(component) is LifecycleState.RUNNING


def test_components_returns_registered_components() -> None:
    # Arrange
    coordinator = LifecycleCoordinator()
    component1 = DummyComponent()
    component2 = DummyComponent()

    coordinator.register(component1)
    coordinator.register(component2)

    # Act
    components = coordinator.components()

    # Assert
    assert component1 in components
    assert component2 in components
    assert len(components) == 2


def test_stop_transitions_running_to_stopped() -> None:
    # Arrange
    coordinator = LifecycleCoordinator()
    component = DummyComponent()

    coordinator.register(component)
    coordinator.initialize()
    coordinator.start()

    # Act
    coordinator.stop()

    # Assert
    assert coordinator.state(component) is LifecycleState.STOPPED


def test_unregister_component() -> None:
    # Arrange
    coordinator = LifecycleCoordinator()
    component = DummyComponent()

    coordinator.register(component)

    # Act
    coordinator.unregister(component)

    # Assert
    with pytest.raises(LifecycleError):
        coordinator.state(component)


def test_unregister_unknown_component_raises_error() -> None:
    # Arrange
    coordinator = LifecycleCoordinator()
    component = DummyComponent()

    # Act / Assert
    with pytest.raises(LifecycleError):
        coordinator.unregister(component)


def test_unregister_running_component_raises_error() -> None:
    # Arrange
    coordinator = LifecycleCoordinator()
    component = DummyComponent()

    coordinator.register(component)
    coordinator.initialize()
    coordinator.start()

    # Act / Assert
    with pytest.raises(LifecycleError):
        coordinator.unregister(component)


def test_initialize_transitions_created_to_initialized() -> None:
    # Arrange
    coordinator = LifecycleCoordinator()
    component = DummyComponent()

    coordinator.register(component)

    # Act
    coordinator.initialize()

    # Assert
    assert coordinator.state(component) is LifecycleState.INITIALIZED


def test_initialize_is_idempotent() -> None:
    # Arrange
    coordinator = LifecycleCoordinator()
    component = DummyComponent()

    coordinator.register(component)
    coordinator.initialize()

    # Act
    coordinator.initialize()

    # Assert
    assert coordinator.state(component) is LifecycleState.INITIALIZED


def test_start_is_idempotent() -> None:
    # Arrange
    coordinator = LifecycleCoordinator()
    component = DummyComponent()

    coordinator.register(component)
    coordinator.initialize()
    coordinator.start()

    # Act
    coordinator.start()

    # Assert
    assert coordinator.state(component) is LifecycleState.RUNNING


def test_stop_is_idempotent() -> None:
    # Arrange
    coordinator = LifecycleCoordinator()
    component = DummyComponent()

    coordinator.register(component)
    coordinator.initialize()
    coordinator.start()
    coordinator.stop()

    # Act
    coordinator.stop()

    # Assert
    assert coordinator.state(component) is LifecycleState.STOPPED


def test_start_from_created_raises_error() -> None:
    # Arrange
    coordinator = LifecycleCoordinator()
    component = DummyComponent()

    coordinator.register(component)

    # Act / Assert
    with pytest.raises(LifecycleError):
        coordinator.start()
