from datetime import datetime
from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums import BaseEnum

if TYPE_CHECKING:
    from src.applications.models import ApplicationModel


class EventFormat(BaseEnum):
    CLASSIC = "classic"
    FAMILY = "family"


class EventModel(BigIntAuditBase):
    """Event model."""

    __tablename__ = "events"

    number: Mapped[int]
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str]
    datetime_event: Mapped[datetime]
    registration_start: Mapped[datetime]
    registration_end: Mapped[datetime]
    duration: Mapped[int]  # event duration in minutes
    location: Mapped[str]

    format: Mapped[EventFormat] = mapped_column(
        SQLEnum(EventFormat, name="event_format"), nullable=False
    )

    price: Mapped[int]
    theme: Mapped[str | None]  # event theme, e.g., "Star Wars"
    max_teams: Mapped[int]
    image_url: Mapped[str | None]

    applications: Mapped[list["ApplicationModel"]] = relationship(
        back_populates="event", cascade="all, delete-orphan"
    )
