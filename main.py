
import uvicorn
from fastapi import FastAPI

from routes.routes import router
from middlewares.log_middleware import log_requests


def create_app() -> FastAPI:
    app = FastAPI()

    # Register middleware
    app.middleware("http")(log_requests)

    # Register routes
    app.include_router(router, prefix="/api")

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        access_log=False,
    )
