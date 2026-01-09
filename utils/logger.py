import logging
import os

def setup_logging():
    """Setup minimal logging for the framework"""
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File handler
    file_handler = logging.FileHandler("logs/automation.log")
    file_handler.setFormatter(formatter)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # Reduce WebDriver Manager logging noise to WARN level
    logging.getLogger('WDM').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)

    return root_logger
