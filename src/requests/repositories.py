from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from .models import RequestModel


class RequestRepository(SQLAlchemyAsyncRepository[RequestModel]):
    """Request repository"""

    model_type = RequestModel
