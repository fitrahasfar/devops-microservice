import redis
from app.core.config import REDIS_URL
from app.core.logging import logger

redis_client = redis.Redis.from_url(REDIS_URL)

def test_redis_connection():
    try:
        redis_client.ping() # Test ping redis
        logger.info("Redis connection successfull")
        return True
    except Exception as e:
        logger.error("Redis connection failed")
        return False