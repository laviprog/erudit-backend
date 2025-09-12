from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.auth.security.schemas import TokenPayload
from src.auth.security.token import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


async def get_current_admin(token: str = Depends(oauth2_scheme)) -> TokenPayload:
    return verify_token(token)


CurrentAdminDep = Annotated[TokenPayload, Depends(get_current_admin)]
