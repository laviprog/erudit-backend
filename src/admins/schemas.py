from datetime import datetime

from src.schemas import BaseSchema

from .models import AdminModel


class Admin(BaseSchema):
    id: int
    username: str
    created_at: datetime


class AdminCreate(BaseSchema):
    username: str
    password: str


class AdminList(BaseSchema):
    admins: list[Admin]

    @classmethod
    def from_orm_list(cls, objs: list[AdminModel]):
        return cls(admins=[Admin.model_validate(obj) for obj in objs])
