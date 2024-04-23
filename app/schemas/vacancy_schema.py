"""Module with "Vacancy" tortoise model."""

from tortoise import fields
from tortoise.models import Model

from app.schemas.employer_schema import Employer


class Vacancy(Model):
    """DB schema for vacancies.

    The main one.
    """

    id = fields.UUIDField(pk=True)
    title = fields.CharField(max_length=255, unique=True)
    employer: fields.ForeignKeyRelation[Employer] = fields.ForeignKeyField("models.Employer", related_name="vacancies")

    def __str__(self) -> str:
        return self.title
