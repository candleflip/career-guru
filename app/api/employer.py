from fastapi import APIRouter

from app.crud.employer import post
from app.models.pydantic.employer import EmployerPayload, EmployerResponse

router = APIRouter()


@router.post("/", response_model=EmployerResponse)
async def create_employer(payload: EmployerPayload) -> EmployerResponse:
    employer_id = await post(payload=payload)
    response = EmployerResponse(id=employer_id, name=payload.name)
    return response
