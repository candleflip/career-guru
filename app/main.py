"""Entrypoint to application."""

from fastapi import FastAPI

from app.api import health_check
from app.init_db import initialize_database


def create_application() -> FastAPI:
    """Create root application.

    Collect all routes

    Returns:
        Ready to run application

    """
    application = FastAPI()
    application.include_router(router=health_check.router, tags=["health-check"])

    return application


app = create_application()


@app.on_event("startup")
def startup_event() -> None:
    """Run instructions on app startup."""
    initialize_database(app=app)
