from advanced_alchemy.exceptions import NotFoundError
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from src.middlewares import LogMiddleware

from .applications.routes import router as applications_router
from .events.routes import router as events_router
from .requests.routes import router as requests_router
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
app.include_router(router=events_router)
app.include_router(router=applications_router)
app.include_router(router=requests_router)


@app.exception_handler(NotFoundError)
async def not_found_handler(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "detail": "Resource not found",
        },
    )
