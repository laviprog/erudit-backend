from typing import Annotated, AsyncGenerator

from fastapi import Depends

from src.applications.services import ApplicationService
from src.database.config import sqlalchemy_config


async def provide_application_service() -> AsyncGenerator[ApplicationService, None]:
    async with ApplicationService.new(config=sqlalchemy_config) as service:
        yield service


ApplicationServiceDep = Annotated[ApplicationService, Depends(provide_application_service)]
