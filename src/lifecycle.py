from contextlib import asynccontextmanager

from fastapi import FastAPI

from src import log
from src.admins.models import AdminModel
from src.admins.services import AdminService
from src.config import settings
from src.database.config import sqlalchemy_config


@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.ADMIN_USERNAME_DEFAULT and settings.ADMIN_PASSWORD_DEFAULT:
        async with AdminService.new(config=sqlalchemy_config) as service:
            existing_admin = await service.get_one_or_none(username=settings.ADMIN_USERNAME_DEFAULT)
            if existing_admin:
                log.info(f"Admin with username {settings.ADMIN_USERNAME_DEFAULT} already exists")
            else:
                await service.create_admin(
                    AdminModel(
                        username=settings.ADMIN_USERNAME_DEFAULT,
                        password=settings.ADMIN_PASSWORD_DEFAULT,
                    )
                )
                log.info(f"Admin with username {settings.ADMIN_USERNAME_DEFAULT} has been created")
    yield
