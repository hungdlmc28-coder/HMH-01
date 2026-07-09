"""Component registry for the Quant Research Platform."""

from __future__ import annotations

from qrp.foundation import BaseComponent, QRPError


class ComponentRegistry:
    """Registry for platform components."""

    def __init__(self) -> None:
        self._components: dict[str, BaseComponent] = {}

    def register(self, component: BaseComponent) -> None:
        """Register a component."""

        if not isinstance(component, BaseComponent):
            raise TypeError("Component must inherit from BaseComponent.")

        if component.name in self._components:
            raise QRPError(f"Component '{component.name}' is already registered.")

        self._components[component.name] = component

    def unregister(self, name: str) -> None:
        """Remove a component from the registry."""

        self._components.pop(name, None)

    def get(self, name: str) -> BaseComponent | None:
        """Return a registered component."""

        return self._components.get(name)

    def list_components(self) -> list[str]:
        """Return registered component names."""

        return sorted(self._components.keys())
