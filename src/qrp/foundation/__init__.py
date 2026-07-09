"""Foundation layer for the Quant Research Platform."""

from .base_component import BaseComponent
from .exceptions import QRPError

__all__ = [
    "BaseComponent",
    "QRPError",
]
