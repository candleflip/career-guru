"""Module with routes to process employers."""

from __future__ import annotations

from fastapi import APIRouter

from app.crud.employer_crud import get_all, post
from app.models.employer_model import EmployerPayload
from app.schemas.employer_schema import EmployerResponse

router = APIRouter()


@router.post("/", response_model=EmployerResponse)
async def create_employer(payload: EmployerPayload) -> EmployerResponse:  # type: ignore
    employer_id = await post(payload=payload)
    response = EmployerResponse(id=employer_id, name=payload.name)
    return response


@router.get("/", response_model=list[EmployerResponse])  # type: ignore
async def read_all_employers() -> list[EmployerResponse]:  # type: ignore
    employers = await get_all()
    return employers
