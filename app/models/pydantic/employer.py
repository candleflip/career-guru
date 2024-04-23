from uuid import UUID

from pydantic import BaseModel


class EmployerPayload(BaseModel):
    name: str


class EmployerResponse(EmployerPayload):
    id: UUID
