from fastapi import APIRouter

from src.admins.dependencies import AdminServiceDep
from src.auth.schemas import Login, Token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    path="/login",
    description="""
        Authenticate admin using a username and password.
        If the credentials are valid, returns a **JWT access token**
    """,
    responses={
        200: {
            "description": "Successfully authenticated",
        },
        401: {
            "description": "Invalid credentials",
        },
        422: {
            "description": "Validation Error",
        },
    },
)
async def login(request: Login, service: AdminServiceDep) -> Token:
    return await service.login(request)
