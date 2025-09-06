from advanced_alchemy.extensions.fastapi import service

from src.applications.models import ApplicationModel
from src.applications.repositories import ApplicationRepository


class ApplicationService(
    service.SQLAlchemyAsyncRepositoryService[ApplicationModel, ApplicationRepository]
):
    """Application Service"""

    repository_type = ApplicationRepository

    def __init__(self, session, **kwargs):
        kwargs.setdefault("auto_commit", True)
        super().__init__(session=session, **kwargs)
