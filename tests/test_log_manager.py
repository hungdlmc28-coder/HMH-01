import logging

from qrp.runtime import LogManager


def test_get_logger_returns_logger() -> None:
    manager = LogManager()

    logger = manager.get_logger("qrp.runtime")

    assert isinstance(logger, logging.Logger)


def test_same_name_returns_same_logger() -> None:
    manager = LogManager()

    logger1 = manager.get_logger("qrp.runtime")
    logger2 = manager.get_logger("qrp.runtime")

    assert logger1 is logger2


def test_different_names_return_different_loggers() -> None:
    manager = LogManager()

    runtime_logger = manager.get_logger("qrp.runtime")
    plugin_logger = manager.get_logger("qrp.plugin")

    assert runtime_logger is not plugin_logger


def test_empty_name_is_supported() -> None:
    manager = LogManager()

    logger = manager.get_logger("")

    assert isinstance(logger, logging.Logger)
