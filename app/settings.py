"""Settings module.

Collects, processes and prepares all settings
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings of the application.

    Get from environment variables and more

    """

    environment: str = Field(default="dev")
    db_url: str = Field()


@lru_cache()
def get_settings() -> Settings:
    """Configure app settings.

    Returns:
        Instance of app settings

    """
    return Settings()
