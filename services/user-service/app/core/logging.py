import logging

# Configure logging format and level
logging.basicConfig(
    level=logging.INFO,                                             # Set log to INFO
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"   # Define log format
)

# Create logger instance
logger = logging.getLogger("user-service")