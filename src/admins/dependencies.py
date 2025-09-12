from typing import Annotated, AsyncGenerator

from fastapi import Depends

from src.database.config import sqlalchemy_config

from .services import AdminService


async def provide_admin_service() -> AsyncGenerator[AdminService, None]:
    async with AdminService.new(config=sqlalchemy_config) as service:
        yield service


AdminServiceDep = Annotated[AdminService, Depends(provide_admin_service)]
