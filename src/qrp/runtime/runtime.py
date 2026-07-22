"""Runtime lifecycle management for the Quant Research Platform."""

from __future__ import annotations

from qrp.foundation import BaseComponent

from .component_registry import ComponentRegistry
from .configuration import Configuration


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
        self._running = True

    def stop(self) -> None:
        """Stop the runtime."""
        if not self._running:
            return

        self.shutdown()
        self._running = False

    def register_component(self, component: object) -> None:
        """Register a component with the runtime."""
        self._registry.register(component)

    def unregister_component(self, component: object) -> None:
        """Unregister a component from the runtime."""
        self._registry.unregister(component)

    def list_components(self) -> list[str]:
        """Return registered component names."""

        return self._registry.list_components()

    @property
    def configuration(self) -> Configuration:
        return self._configuration

    @property
    def registry(self) -> ComponentRegistry:
        return self._registry
