import logging
import os

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)  # Ensure logs folder exists

logging.basicConfig(
    filename=os.path.join(log_dir, "etl_pipeline.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_logger(name):
    return logging.getLogger(name)
