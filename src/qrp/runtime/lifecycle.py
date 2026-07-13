from __future__ import annotations

from enum import Enum, auto

from qrp.foundation import QRPError


class LifecycleState(Enum):
    """Lifecycle states for runtime-managed components."""

    CREATED = auto()
    INITIALIZED = auto()
    RUNNING = auto()
    STOPPED = auto()


class LifecycleError(QRPError):
    """Raised when an invalid lifecycle operation is attempted."""
