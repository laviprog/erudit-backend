from advanced_alchemy.extensions.fastapi import service

from .models import RequestModel
from .repositories import RequestRepository


class RequestService(service.SQLAlchemyAsyncRepositoryService[RequestModel, RequestRepository]):
    """Request Service"""

    repository_type = RequestRepository

    def __init__(self, session, **kwargs):
        kwargs.setdefault("auto_commit", True)
        super().__init__(session=session, **kwargs)
