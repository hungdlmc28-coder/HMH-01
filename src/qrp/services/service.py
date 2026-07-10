"""Base service abstraction for the Quant Research Platform."""

from __future__ import annotations

from qrp.foundation import BaseComponent


class Service(BaseComponent):
    """Base class for all QRP services."""

    def __init__(self, name: str | None = None) -> None:
        super().__init__(name)
