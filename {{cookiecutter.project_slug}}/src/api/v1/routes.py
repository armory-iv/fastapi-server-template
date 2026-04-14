"""API v1 routes."""

from importlib.metadata import PackageNotFoundError, version

from fastapi import APIRouter

from src.schemas.health import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Return service health and current version."""
    try:
        v = version("{{cookiecutter.project_slug}}")
    except PackageNotFoundError:
        v = "0.1.0"
    return HealthResponse(status="ok", version=v)
