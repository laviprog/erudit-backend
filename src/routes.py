from fastapi import APIRouter

from src.schemas import HealthCheck

router = APIRouter(tags=["Monitoring"])


@router.get(
    "/healthcheck",
    summary="Health Check",
    description="""
        Checks whether the API service is operational and responding
    """,
    responses={
        200: {
            "description": "Service is running",
        },
    },
)
async def healthcheck() -> HealthCheck:
    return HealthCheck()
