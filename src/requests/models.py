from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.enums import BaseEnum


class TypeRequest(BaseEnum):
    CONSULTATION = "consultation"
    PARTNERSHIP = "partnership"
    EVENT_GAME_ORDER = "event_game_order"


class StatusRequest(BaseEnum):
    NEW = "new"
    VIEWED = "viewed"
    PROCESSED = "processed"


class RequestModel(BigIntAuditBase):
    """User Request model."""

    __tablename__ = "requests"

    name: Mapped[str] = mapped_column(String(127))
    email: Mapped[str | None] = mapped_column(String(255))
    phone: Mapped[str | None] = mapped_column(String(255))
    message: Mapped[str | None]
    type: Mapped[TypeRequest | None] = mapped_column(
        SQLEnum(TypeRequest, name="type_request"), nullable=True
    )
    status: Mapped[StatusRequest] = mapped_column(
        SQLEnum(StatusRequest, name="status_request"), nullable=False, default=StatusRequest.NEW
    )
