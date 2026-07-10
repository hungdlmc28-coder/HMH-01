"""Logging manager for the Quant Research Platform."""

from __future__ import annotations

import logging


class LogManager:
    """Provides access to named loggers."""

    def get_logger(self, name: str) -> logging.Logger:
        """Return a logger for the given namespace."""
        return logging.getLogger(name)
