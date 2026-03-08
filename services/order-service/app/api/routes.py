from fastapi import APIRouter
from app.db.database import test_db_connection
from app.db.redis import test_redis_connection
from app.core.config import USER_SERVICE_URL
import requests

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "database": test_db_connection(),
        "redis": test_redis_connection()
    }

@router.get("/orders")
def get_order():
    # Call user-service health enpoint
    user_reponse = requests.get(f"{USER_SERVICE_URL}/health")
    
    return {
        "order_service": "Order service running",
        "user_service_status": user_reponse.json()
    }