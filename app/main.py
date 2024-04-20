"""Entrypoint to application."""

from fastapi import FastAPI

from app.api import health_check


def create_application() -> FastAPI:
    """Creates root application.

    Collects all routes

    Returns:
        Ready to run application

    """
    application = FastAPI()
    application.include_router(router=health_check.router, tags=["health-check"])

    return application


app = create_application()
