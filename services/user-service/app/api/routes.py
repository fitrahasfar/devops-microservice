from fastapi import APIRouter
from app.db.database import test_db_connection
from app.db.redis import test_redis_connection

router = APIRouter()                    # Create router intance

@router.get("/health")                  # Health check endpoint
def health_check():
    db_status = test_db_connection()
    redis_status = test_redis_connection()
    
    return {
        "database": db_status,          # Return DB status
        "redis": redis_status           # Return redis status
    }