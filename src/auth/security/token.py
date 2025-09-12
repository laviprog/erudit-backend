from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from fastapi import HTTPException, status

from src.auth.security.schemas import TokenPayload
from src.config import settings


def _create_token(data: dict[str, Any]) -> str:
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({"exp": expire})
    return jwt.encode(payload, key=settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def create_access_token(token_payload: TokenPayload) -> str:
    data = token_payload.model_dump()
    return _create_token(data)


def _parse_token_payload(payload: dict[str, Any]) -> TokenPayload:
    admin_id = int(payload.get("id"))
    if not admin_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return TokenPayload(id=admin_id)


def _verify_jwt_token(
    token: str,
) -> TokenPayload:
    try:
        payload = jwt.decode(
            token,
            key=settings.SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
        )
        return _parse_token_payload(payload)
    except jwt.ExpiredSignatureError as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired"
        ) from err
    except jwt.InvalidTokenError as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        ) from err


def verify_token(token: str) -> TokenPayload:
    return _verify_jwt_token(token)
