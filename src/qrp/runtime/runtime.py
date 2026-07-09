"""Runtime lifecycle management for the Quant Research Platform."""

from __future__ import annotations

from qrp.foundation import BaseComponent


class Runtime(BaseComponent):
    """Runtime lifecycle controller."""

    def __init__(self, name: str = "Runtime") -> None:
        super().__init__(name=name)
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
