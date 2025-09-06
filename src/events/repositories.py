from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from .models import EventModel


class EventRepository(SQLAlchemyAsyncRepository[EventModel]):
    """Event repository"""

    model_type = EventModel
