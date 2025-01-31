import logging
import os
from logging.handlers import RotatingFileHandler

# Define log directory
log_dir = "logs"

# Define log files
log_files = {
    "etl_pipeline": os.path.join(log_dir, "etl_pipeline.log"),
    "load_errors": os.path.join(log_dir, "load_errors.log"),
    "transform_errors": os.path.join(log_dir, "transform_errors.log"),
    "query_performance": os.path.join(log_dir, "query_performance.log"),
    "visualization_errors": os.path.join(log_dir, "visualization_errors.log"),
}

# Log format
log_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
formatter = logging.Formatter(log_format)

# Function to configure a logger
def setup_logger(name, log_file, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # File handler with log rotation (max 5MB per file, keeps 3 backups)
    file_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=3)
    file_handler.setFormatter(formatter)
    
    # Console handler (prints logs to the terminal)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Avoid duplicate handlers if the logger already has them
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Initialize loggers
etl_logger = setup_logger("ETL_PIPELINE", log_files["etl_pipeline"])
load_logger = setup_logger("LOAD_ERRORS", log_files["load_errors"], logging.ERROR)
transform_logger = setup_logger("TRANSFORM_ERRORS", log_files["transform_errors"], logging.WARNING)
query_logger = setup_logger("QUERY_PERFORMANCE", log_files["query_performance"], logging.DEBUG)
visualization_logger = setup_logger("VISUALIZATION_ERRORS", log_files["visualization_errors"], logging.ERROR)

# Function to get the appropriate logger
def get_logger(name):
    loggers = {
        "ETL_PIPELINE": etl_logger,
        "LOAD_ERRORS": load_logger,
        "TRANSFORM_ERRORS": transform_logger,
        "QUERY_PERFORMANCE": query_logger,
        "VISUALIZATION_ERRORS": visualization_logger,
    }
    return loggers.get(name, etl_logger)  # Default to ETL logger if name not found


