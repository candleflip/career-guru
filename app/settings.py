"""Settings module.

Collects, processes and prepares all settings
"""

from functools import lru_cache
from typing import Literal

from pydantic import computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings of the application.

    Get from environment variables and more

    """

    ENVIRONMENT: Literal["dev", "test", "prod"] = "dev"
    POSTGRES_SCHEMA: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DATABASE_NAME: str

    @computed_field  # type: ignore[misc]
    @property
    def POSTGRES_URL(self) -> str:
        """Construct full Postgres URL"""
        return (
            f"{self.POSTGRES_SCHEMA}://"
            f"{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DATABASE_NAME}"
        )


@lru_cache()
def get_settings() -> Settings:
    """Configure app settings.

    Returns:
        Instance of app settings

    """
    return Settings()
