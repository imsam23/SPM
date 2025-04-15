import logging
import os

def setup_logger(name: str, log_file: str = "app.log", level: str = "INFO") -> logging.Logger:
    """
    Sets up a logger that logs to both the console and a file.

    Args:
        name (str): Name of the logger.
        log_file (str): Path to the log file.
        level (str): Logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Ensure no duplicate handlers
    if not logger.hasHandlers():
        # Create a file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        # Define a log format
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Example usage
if __name__ == "__main__":
    logger = setup_logger("StockPriceMonitor", log_file="stock_price_monitor.log", level="DEBUG")
    logger.info("Logger is set up and ready to use!")
    logger.debug("This is a debug message.")
    logger.error("This is an error message.")
