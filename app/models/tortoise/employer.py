from tortoise import fields
from tortoise.models import Model


class Employer(Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
