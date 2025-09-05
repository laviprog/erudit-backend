import structlog
from starlette.middleware.base import BaseHTTPMiddleware

from src.logging import generate_correlation_id


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        structlog.contextvars.bind_contextvars(
            correlation_id=generate_correlation_id(),
            method=request.method,
            path=request.url.path,
            ip_address=request.client.host,
        )

        response = await call_next(request)

        structlog.contextvars.unbind_contextvars("correlation_id", "method", "path", "ip_address")

        return response
