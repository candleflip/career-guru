from uuid import UUID

from app.models.pydantic.employer import EmployerPayload
from app.models.tortoise.employer import Employer


async def post(payload: EmployerPayload) -> UUID:
    employer = Employer(name=payload.name)
    await employer.save()
    return employer.id
