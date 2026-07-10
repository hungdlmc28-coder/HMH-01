"""Base plugin abstraction for the Quant Research Platform."""

from __future__ import annotations

from qrp.foundation import BaseComponent


class Plugin(BaseComponent):
    """Base class for all QRP plugins."""

    def __init__(self, name: str | None = None) -> None:
        super().__init__(name)
