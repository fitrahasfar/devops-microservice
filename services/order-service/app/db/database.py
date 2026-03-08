from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL
from app.core.logging import logger

# Create engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def test_db_connection():
    try:
        connection = engine.connect()   # Attempt connection
        connection.close()              # Close if successful
        logger.info("Order DB connection successful")
        return True
    except Exception as e:
        logger.error(f"Order DB connection failed: {e}")
        return False