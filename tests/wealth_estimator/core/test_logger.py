import logging
from wealth_estimator.core.logger import Logger

def test_returns_logger_instance():
    log = Logger.get_logger("test_logger_1")
    assert isinstance(log, logging.Logger)
    assert log.name == "test_logger_1"

def test_logger_has_console_handler():
    log = Logger.get_logger("test_logger_2")
    handlers = [h for h in log.handlers if isinstance(h, logging.StreamHandler)]
    assert len(handlers) >= 1

def test_logger_does_not_duplicate_handlers():
    log1 = Logger.get_logger("test_logger_3")
    num_handlers_before = len(log1.handlers)

    log2 = Logger.get_logger("test_logger_3")
    num_handlers_after = len(log2.handlers)

    assert log1 is log2  # Same logger instance reused
    assert num_handlers_before == num_handlers_after  # No new handlers added

def test_logger_respects_log_level():
    log = Logger.get_logger("test_logger_4", log_level=logging.DEBUG)
    assert log.level == logging.DEBUG

