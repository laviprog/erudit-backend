from typing import Annotated, AsyncGenerator

from fastapi import Depends

from src.database.config import sqlalchemy_config

from .services import RequestService


async def provide_request_service() -> AsyncGenerator[RequestService, None]:
    async with RequestService.new(config=sqlalchemy_config) as service:
        yield service


RequestServiceDep = Annotated[RequestService, Depends(provide_request_service)]
