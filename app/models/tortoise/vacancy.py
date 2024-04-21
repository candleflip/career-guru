from tortoise import fields
from tortoise.models import Model
from app.models.tortoise.employer import Employer


class Vacancy(Model):
    id = fields.UUIDField(pk=True)
    title = fields.CharField(max_length=255, unique=True)
    employer: fields.ForeignKeyRelation[Employer] = fields.ForeignKeyField("models.Employer", related_name="vacancies")

    def __str__(self):
        return self.title
