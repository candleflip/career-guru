"""Module with Pydantic modules for employers."""

from pydantic import BaseModel


class EmployerPayload(BaseModel):
    """Model for employer passed to the app upon request."""

    name: str
