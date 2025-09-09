from datetime import datetime, timezone
from typing import Sequence

from advanced_alchemy.extensions.fastapi import service

from src.events.models import EventModel
from src.events.repositories import EventRepository


class EventService(service.SQLAlchemyAsyncRepositoryService[EventModel, EventRepository]):
    """Event Service"""

    repository_type = EventRepository

    def __init__(self, session, **kwargs):
        kwargs.setdefault("auto_commit", True)
        super().__init__(session=session, **kwargs)

    async def get_events(self, actual: bool = False) -> Sequence[EventModel]:
        filters = [EventModel.datetime_event >= datetime.now(tz=timezone.utc)] if actual else []
        return await self.list(*filters, order_by=(EventModel.datetime_event, False))
