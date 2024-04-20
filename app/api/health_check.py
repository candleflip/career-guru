from fastapi import APIRouter

router = APIRouter()


@router.get("/health-check")
def health_check() -> dict[str, str]:
    return {"ping": "pong"}
