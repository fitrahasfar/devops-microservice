import os
from dotenv import load_dotenv

load_dotenv()                                   # Load .env

DATABASE_URL = os.getenv("DATABASE_URL")        # Get database URL
REDIS_URL = os.getenv("REDIS_URL")              # Get redis URL
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL")    # Get user service URL