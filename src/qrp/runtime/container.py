"""Dependency injection container for the Quant Research Platform."""

from __future__ import annotations

from qrp.foundation import QRPError


class Container:
    """Simple dependency injection container."""

    def __init__(self) -> None:
        self._instances: dict[str, object] = {}

    def register_instance(self, name: str, instance: object) -> None:
        """Register a singleton instance."""
        if name in self._instances:
            raise QRPError(f"Dependency '{name}' is already registered.")

        self._instances[name] = instance

    def resolve(self, name: str) -> object:
        """Resolve a registered instance."""
        try:
            return self._instances[name]
        except KeyError as exc:
            raise QRPError(f"Dependency '{name}' is not registered.") from exc

    def contains(self, name: str) -> bool:
        """Return whether a dependency is registered."""
        return name in self._instances
