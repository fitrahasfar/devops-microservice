import redis
from app.core.config import REDIS_URL
from app.core.logging import logger

# Create redis client
redis_client = redis.Redis.from_url(REDIS_URL)

# Function to test Redis connection
def test_redis_connection():
    try:
        redis_client.ping()
        logger.info("Redis connection successful")
        return True
    except Exception as e:
        logger.error("Redis connection failed: {e}")
        return False