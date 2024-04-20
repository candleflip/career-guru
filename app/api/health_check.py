"""Simple route to check application viability."""

from fastapi import APIRouter, Depends

from app.settings import Settings, get_settings

router = APIRouter()


@router.get("/health-check")
def health_check(settings: Settings = Depends(get_settings)) -> dict[str, str]:
    """Check if application is alive.

    Returns:
        Metadata dict if alive

    """
    return {"running?": "yes", "environment": settings.environment}
