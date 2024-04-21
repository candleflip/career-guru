"""Module with "Employer" tortoise model."""

from tortoise import fields
from tortoise.models import Model


class Employer(Model):
    """Model for employers who posted vacancies."""

    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
