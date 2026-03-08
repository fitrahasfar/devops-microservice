from fastapi import FastAPI
from app.api.routes import router
from app.core.logging import logger

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
def startup_event():
    logger.info("Order service started successfully")