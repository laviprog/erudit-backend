from datetime import datetime

from src.schemas import BaseSchema

from .models import RequestModel, StatusRequest, TypeRequest


class Request(BaseSchema):
    id: int
    name: str
    email: str | None
    phone: str | None
    message: str | None
    type: TypeRequest | None
    status: StatusRequest
    created_at: datetime


class RequestCreate(BaseSchema):
    name: str
    email: str | None
    phone: str | None
    message: str | None
    type: TypeRequest | None


class RequestList(BaseSchema):
    applications: list[Request]

    @classmethod
    def from_orm_list(cls, objs: list[RequestModel]):
        return cls(applications=[Request.model_validate(obj) for obj in objs])
