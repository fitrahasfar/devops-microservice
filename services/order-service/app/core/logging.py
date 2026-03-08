import logging

logging.basicConfig(
    level=logging.INFO, # Set log
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"   # Set Format
)

logger = logging.getLogger("order-service") # Create logger