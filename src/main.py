from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.middlewares import LogMiddleware

from .logging import configure as configure_logging
from .routes import router

configure_logging()

app = FastAPI(
    title="Erudit API",
    version="0.0.1",
    docs_url="/docs",
    openapi_url="/openapi.json",
    root_path="/api/v1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(LogMiddleware)

app.include_router(router=router)
