"""Exception hierarchy for the Quant Research Platform."""

from __future__ import annotations


class QRPError(Exception):
    """Base error for all QRP-specific errors."""

    def __init__(self, message: str = "An unknown QRP error occurred.") -> None:
        super().__init__(message)
