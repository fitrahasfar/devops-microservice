from fastapi import FastAPI
from app.api.routes import router
from app.core.logging import logger

app = FastAPI()                                     # Create FastApi Intance

app.include_router(router)                          # Include APi routes

@app.on_event("startup")                            # Run on startup
def startup_event():
    logger.info("User service stated seccessfully") # Log Startup