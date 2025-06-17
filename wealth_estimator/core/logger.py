import logging

class Logger:
    @staticmethod
    def get_logger(name: str, log_level=logging.INFO) -> logging.Logger:
        logger = logging.getLogger(name)
        
        # Prevent adding multiple handlers if logger already configured
        if logger.handlers:
            return logger
        
        logger.setLevel(log_level)

        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        return logger