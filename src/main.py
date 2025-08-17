
from fastapi import FastAPI
from logger import logger
from middleware import log_requests
from starlette.middleware.base import BaseHTTPMiddleware





app = FastAPI()
logger.info("Starting the application...")

app.add_middleware(BaseHTTPMiddleware, dispatch=log_requests)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/upload-videos')
async def upload_videos():
    return {}