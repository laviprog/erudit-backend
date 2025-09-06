from datetime import datetime

from src.applications.models import ApplicationModel
from src.schemas import BaseSchema


class Application(BaseSchema):
    id: int
    captain_name: str
    captain_email: str
    captain_phone: str
    teamName: str
    teamParticipantsNumber: int
    created_at: datetime
    updated_at: datetime
    event_id: int


class ApplicationCreate(BaseSchema):
    captain_name: str
    captain_email: str
    captain_phone: str
    teamName: str
    teamParticipantsNumber: int
    event_id: int


class ApplicationList(BaseSchema):
    applications: list[Application]

    @classmethod
    def from_orm_list(cls, objs: list[ApplicationModel]):
        return cls(applications=[Application.model_validate(obj) for obj in objs])
