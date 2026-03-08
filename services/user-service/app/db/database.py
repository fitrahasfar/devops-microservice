from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL
from app.core.logging import logger

# Create database engine
engine = create_engine(DATABASE_URL)

# Create sessions factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)

# Function to test database connection
def test_db_connection():
    try:
        connection = engine.connect()                       # Try connection to database
        connection.close()                                  # Close connection if successful
        logger.info("Database connection successful")       # Log Success
        return True
    except Exception as e:
        logger.error(f"Database connection failed: {e}")    # Log Error
        return False