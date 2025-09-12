from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from .models import AdminModel


class AdminRepository(SQLAlchemyAsyncRepository[AdminModel]):
    """Admin repository"""

    model_type = AdminModel
