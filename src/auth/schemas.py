from src.schemas import BaseSchema


class Token(BaseSchema):
    access_token: str
    token_type: str = "bearer"


class Login(BaseSchema):
    username: str
    password: str
