from typing import TYPE_CHECKING

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from src.events.models import EventModel


class ApplicationModel(BigIntAuditBase):
    """Application model."""

    __tablename__ = "applications"

    captain_name: Mapped[str] = mapped_column(String(255))
    captain_email: Mapped[str] = mapped_column(String(255))
    captain_phone: Mapped[str] = mapped_column(String(31))
    teamName: Mapped[str] = mapped_column(String(255))
    teamParticipantsNumber: Mapped[int]

    event_id: Mapped[int] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"))
    event: Mapped["EventModel"] = relationship(back_populates="applications")
