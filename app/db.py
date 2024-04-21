"""Module with functions for database preparing."""

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.settings import Settings, get_settings


def initialize_database(app: FastAPI, settings: Settings = get_settings()) -> None:
    """Initialize database for the FastAPI app.

    Args:
        app: FastAPI app
        settings: fetched settings

    """
    register_tortoise(
        app=app,
        db_url=settings.db_url,
        modules={
            "models": [
                "app.models.tortoise.vacancy",
                "app.models.tortoise.employer",
            ]
        },
        generate_schemas=True,
        add_exception_handlers=True,
    )
