from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class AdminModel(BigIntAuditBase):
    """Admin model."""

    __tablename__ = "admins"

    username: Mapped[str] = mapped_column(String(127))
    password: Mapped[str] = mapped_column(String(255))
