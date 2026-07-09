"""Base component for the Quant Research Platform."""

from __future__ import annotations

import logging


class BaseComponent:
    """Base class for all platform components.

    Provides a common identity, logger and lifecycle that can be
    shared across runtime, infrastructure, plugins and services.
    """

    def __init__(self, name: str | None = None) -> None:
        self._name = name or self.__class__.__name__
        self._initialized = False
        self._logger = logging.getLogger(f"qrp.{self._name}")

    @property
    def name(self) -> str:
        """Return the component name."""
        return self._name

    @property
    def logger(self) -> logging.Logger:
        """Return the component logger."""
        return self._logger

    @property
    def is_initialized(self) -> bool:
        """Return the initialization state."""
        return self._initialized

    def initialize(self) -> None:
        """Initialize the component."""
        self._initialized = True

    def shutdown(self) -> None:
        """Shutdown the component."""
        self._initialized = False
