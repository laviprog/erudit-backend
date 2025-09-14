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


class EventUpdate(EventCreate): ...


class EventPartialUpdate(BaseSchema):
    number: int | None = None
    title: str | None = None
    description: str | None = None
    datetime_event: datetime | None = None
    registration_start: datetime | None = None
    registration_end: datetime | None = None
    duration: int | None = None
    location: str | None = None
    format: EventFormat | None = None
    price: int | None = None
    theme: str | None = None
    max_teams: int | None = None
    image_url: str | None = None


class EventList(BaseSchema):
    events: list[Event]

    @classmethod
    def from_orm_list(cls, objs: list[EventModel]):
        return cls(events=[Event.model_validate(obj) for obj in objs])
