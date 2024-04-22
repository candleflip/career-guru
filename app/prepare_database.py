"""Module with functions for database preparing."""

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.settings import Settings, get_settings

settings: Settings = get_settings()


TORTOISE_ORM = {
    "connections": {"default": settings.db_url},
    "apps": {
        "models": {
            "models": [
                "app.models.tortoise.vacancy",
                "app.models.tortoise.employer",
                "aerich.models",
            ],
            "default_connection": "default",
        }
    },
}


def prepare_database_for_app(app: FastAPI) -> None:
    """Initialize database for the FastAPI app.

    Args:
        app: FastAPI app

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
        generate_schemas=False,
        add_exception_handlers=True,
    )
