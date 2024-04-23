from __future__ import annotations

from uuid import UUID

from app.models.pydantic.employer_model import EmployerPayload
from app.models.tortoise.employer_schema import Employer


async def post(payload: EmployerPayload) -> UUID:
    employer = Employer(name=payload.name)
    await employer.save()
    return employer.id


async def get_all() -> list[dict[str, str | UUID]]:
    employers = await Employer.all().values()
    return employers
