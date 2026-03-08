import os
from dotenv import load_dotenv

# Load environment variables .env file
load_dotenv()

# Database URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Redis URL from .env
REDIS_URL = os.getenv("REDIS_URL")