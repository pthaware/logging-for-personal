
import logging
import time

from fastapi import Request

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: - %(message)s"
)

logger = logging.getLogger(__name__)


async def log_requests(request: Request, call_next):
    start_time = time.perf_counter()

    logger.info(
        f"Incoming request: {request.method} {request.url.path}"
    )

    try:
        response = await call_next(request)

        process_time = time.perf_counter() - start_time

        logger.info(
            f"Completed: {request.method} {request.url.path} "
            f"| Status: {response.status_code} "
            f"| Duration: {process_time:.4f}s"
        )

        response.headers["X-Process-Time"] = str(process_time)
        return response

    except Exception:
        logger.exception(
            f"Request failed: {request.method} {request.url.path}"
        )
        raise
