"""Simple route to check application viability."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health-check")
def health_check() -> dict[str, str]:
    """Checks if application is alive.

    Returns:
        Simple dict if alive

    """
    return {"ping": "pong"}
