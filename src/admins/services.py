from advanced_alchemy.extensions.fastapi import service
from fastapi import HTTPException, status

from src.auth.schemas import Login, Token

from ..auth.security.passwords import hash_password, verify_password
from ..auth.security.schemas import TokenPayload
from ..auth.security.token import create_access_token
from .models import AdminModel
from .repositories import AdminRepository


class AdminService(service.SQLAlchemyAsyncRepositoryService[AdminModel, AdminRepository]):
    """Admin Service"""

    repository_type = AdminRepository

    def __init__(self, session, **kwargs):
        kwargs.setdefault("auto_commit", True)
        super().__init__(session=session, **kwargs)

    async def create_admin(self, admin: AdminModel) -> AdminModel:
        admin.password = hash_password(admin.password)
        return await self.create(admin)

    async def login(self, admin_data: Login) -> Token:
        admin = await self.get_one_or_none(username=admin_data.username)

        if admin is None or not verify_password(admin_data.password, admin.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        payload = TokenPayload(id=admin.id)
        access_token = create_access_token(payload)
        return Token(
            access_token=access_token,
            token_type="bearer",
        )
