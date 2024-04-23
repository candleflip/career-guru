"""Module with "Employer" tortoise model."""

from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Employer(Model):
    """Model for employers who posted vacancies."""

    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


EmployerResponse = pydantic_model_creator(cls=Employer)
