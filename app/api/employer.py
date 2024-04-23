from __future__ import annotations

from fastapi import APIRouter

from app.crud.employer import get_all, post
from app.models.pydantic.employer_model import EmployerPayload
from app.models.tortoise.employer_schema import EmployerResponse

router = APIRouter()


@router.post("/", response_model=EmployerResponse)
async def create_employer(payload: EmployerPayload) -> EmployerResponse:
    employer_id = await post(payload=payload)
    response = EmployerResponse(id=employer_id, name=payload.name)
    return response


@router.get("/", response_model=list[EmployerResponse])
async def read_all_employers() -> list[EmployerResponse]:
    employers = await get_all()
    return employers
