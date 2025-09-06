from fastapi import APIRouter, status

from src.applications.dependencies import ApplicationServiceDep
from src.applications.models import ApplicationModel
from src.applications.schemas import Application, ApplicationCreate, ApplicationList

router = APIRouter(prefix="/applications", tags=["Applications"])


@router.get(
    "",
    summary="List all applications",
    description="Retrieve a list of all applications",
    responses={
        status.HTTP_200_OK: {"description": "List of all applications returned successfully"},
    },
)
async def get_all_applications(service: ApplicationServiceDep) -> ApplicationList:
    applications = await service.list()
    return ApplicationList.from_orm_list(applications)


@router.get(
    "/{application_id}",
    summary="Get application by ID",
    description="Retrieve a specific application by its ID",
    responses={
        status.HTTP_200_OK: {"description": "Application returned successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Application not found"},
    },
)
async def get_application_by_id(application_id: int, service: ApplicationServiceDep) -> Application:
    application = await service.get(application_id)
    return Application.model_validate(application)


@router.post(
    "",
    summary="Create a new application",
    description="Create a new application",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"description": "Application created successfully"},
    },
)
async def create_new_application(
    application: ApplicationCreate, service: ApplicationServiceDep
) -> Application:
    application_model = ApplicationModel(**application.to_dict())
    application_created = await service.create(application_model)
    return Application.model_validate(application_created)
