from pydantic import BaseModel


class EmployerPayload(BaseModel):
    name: str
