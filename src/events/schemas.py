from datetime import datetime

from src.events.models import EventFormat, EventModel
from src.schemas import BaseSchema


class Event(BaseSchema):
    id: int
    number: int
    title: str
    description: str
    datetime_event: datetime
    registration_start: datetime
    registration_end: datetime
    duration: int
    location: str
    format: EventFormat | None
    price: int
    theme: str | None
    max_teams: int
    image_url: str | None
    created_at: datetime
    updated_at: datetime


class EventCreate(BaseSchema):
    number: int
    title: str
    description: str
    datetime_event: datetime
    registration_start: datetime
    registration_end: datetime
    duration: int
    location: str
    format: EventFormat | None
    price: int
    theme: str | None
    max_teams: int
    image_url: str | None


class EventList(BaseSchema):
    events: list[Event]

    @classmethod
    def from_orm_list(cls, objs: list[EventModel]):
        return cls(events=[Event.model_validate(obj) for obj in objs])
