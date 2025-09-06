from typing import Annotated, AsyncGenerator

from fastapi import Depends

from src.database.config import sqlalchemy_config
from src.events.services import EventService


async def provide_event_service() -> AsyncGenerator[EventService, None]:
    async with EventService.new(config=sqlalchemy_config) as service:
        yield service


EventServiceDep = Annotated[EventService, Depends(provide_event_service)]
