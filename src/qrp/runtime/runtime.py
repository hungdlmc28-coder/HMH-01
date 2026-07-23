"""Runtime lifecycle management for the Quant Research Platform."""

from __future__ import annotations

from qrp.foundation import BaseComponent

from .component_registry import ComponentRegistry
from .configuration import Configuration
from .lifecycle import LifecycleState
from .lifecycle_coordinator import LifecycleCoordinator


class Runtime(BaseComponent):
    """Runtime lifecycle controller."""

    def __init__(
        self,
        configuration: Configuration,
        registry: ComponentRegistry,
        name: str | None = None,
    ) -> None:
        super().__init__(name)

        self._configuration = configuration
        self._registry = registry
        self._lifecycle = LifecycleCoordinator()
        self._running = False

    @property
    def is_running(self) -> bool:
        """Return whether the runtime is currently running."""
        return self._running

    def start(self) -> None:
        """Start the runtime."""
        if self._running:
            return

        self.initialize()
        self.initialize_components()
        self.start_components()
        self._running = True

    def stop(self) -> None:
        """Stop the runtime."""
        if not self._running:
            return

        self.stop_components()
        self.shutdown()
        self._running = False

    def register_component(self, component: object) -> None:
        """Register a component with the runtime."""
        self._registry.register(component)
        self._lifecycle.register(component)

    def initialize_components(self) -> None:
        """Initialize all registered components."""
        self._lifecycle.initialize()

    def start_components(self) -> None:
        """Start all initialized components."""
        self._lifecycle.start()

    def stop_components(self) -> None:
        """Stop all running components."""
        self._lifecycle.stop()

    def unregister_component(self, name: str) -> None:
        """Unregister a component from the runtime."""
        component = self._registry.get(name)
        if component is None:
            return

        self._registry.unregister(name)
        self._lifecycle.unregister(component)

    def list_components(self) -> list[str]:
        """Return registered component names."""

        return self._registry.list_components()

    def lifecycle_state(self, component: object) -> LifecycleState:
        """Return the lifecycle state of a component."""

        return self._lifecycle.state(component)

    @property
    def configuration(self) -> Configuration:
        return self._configuration

    @property
    def registry(self) -> ComponentRegistry:
        return self._registry
