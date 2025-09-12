from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.middlewares import LogMiddleware

from .admins.routes import router as admins_router
from .applications.routes import router as applications_router
from .auth.routes import router as auth_router
from .events.routes import router as events_router
from .exceptions.handlers import setup_exception_handlers
from .exceptions.responses import error_responses
from .lifecycle import lifespan
from .logging import configure as configure_logging
from .requests.routes import router as requests_router
from .routes import router

configure_logging()

app = FastAPI(
    title="Erudit API",
    version="0.0.1",
    docs_url="/docs",
    openapi_url="/openapi.json",
    root_path="/api/v1",
    responses=error_responses,
    lifespan=lifespan,
)

setup_exception_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(LogMiddleware)

app.include_router(router=router)
app.include_router(router=events_router)
app.include_router(router=applications_router)
app.include_router(router=requests_router)
app.include_router(router=admins_router)
app.include_router(router=auth_router)
