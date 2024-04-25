"""Module with functions for database preparing."""

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.settings import Settings, get_settings

settings: Settings = get_settings()


TORTOISE_ORM = {
    "connections": {"default": settings.POSTGRES_URL},
    "apps": {
        "models": {
            "models": [
                "app.schemas.vacancy_schema",
                "app.schemas.employer_schema",
                "aerich.models",
            ],
            "default_connection": "default",
        }
    },
}


def prepare_database_for_app(app: FastAPI) -> None:
    """Initialize db for the FastAPI app.

    Args:
        app: FastAPI app

    """
    register_tortoise(
        app=app,
        db_url=settings.POSTGRES_URL,
        modules={
            "models": [
                "app.schemas.vacancy_schema",
                "app.schemas.employer_schema",
            ]
        },
        generate_schemas=False,
        add_exception_handlers=True,
    )
