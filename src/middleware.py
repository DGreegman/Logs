from fastapi import Request
from logger import logger
import time

async def log_requests(request:Request, call_next):
    start = time.time()
   
    response = await call_next(request)
    process_time = time.time() - start
    
    log_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "client": request.client,
        "process_time": round(process_time, 2),
        "status_code": response.status_code,
    }
    logger.info(log_info, extra=log_info)
    return response