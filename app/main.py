"""Entrypoint to application."""

from fastapi import FastAPI

from app.api import employer, health_check
from app.db.prepare_database import prepare_database_for_app as prepare_db


def create_application() -> FastAPI:
    """Create root application.

    Collect all routes

    Returns:
        Ready to run application

    """
    application = FastAPI()
    application.include_router(router=health_check.router, tags=["health-check"])
    application.include_router(router=employer.router, prefix="/employers", tags=["employers"])

    return application


app = create_application()


@app.on_event("startup")
def startup_event() -> None:
    """Run instructions on app startup."""
    prepare_db(app=app)
