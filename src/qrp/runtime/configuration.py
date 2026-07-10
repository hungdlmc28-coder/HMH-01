"""Configuration system for the Quant Research Platform."""

from __future__ import annotations

from typing import Any


class Configuration:
    """Simple in-memory configuration store."""

    def __init__(self) -> None:
        self._values: dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value."""
        self._values[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Return a configuration value."""
        return self._values.get(key, default)

    def has(self, key: str) -> bool:
        """Return whether the configuration key exists."""
        return key in self._values

    def remove(self, key: str) -> None:
        """Remove a configuration value."""
        self._values.pop(key, None)

    def clear(self) -> None:
        """Remove all configuration values."""
        self._values.clear()
