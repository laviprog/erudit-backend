from fastapi import APIRouter, status

from ..auth.security.dependencies import CurrentAdminDep
from .dependencies import RequestServiceDep
from .models import RequestModel
from .schemas import Request, RequestCreate, RequestList, RequestPartialUpdate

router = APIRouter(prefix="/requests", tags=["Requests"])


@router.get(
    "",
    summary="List all requests",
    description="Retrieve a list of all requests",
    responses={
        status.HTTP_200_OK: {"description": "List of all requests returned successfully"},
    },
)
async def get_all_requests(
    service: RequestServiceDep,
    cur_admin: CurrentAdminDep,
) -> RequestList:
    requests = await service.list()
    return RequestList.from_orm_list(requests)


@router.get(
    "/{request_id}",
    summary="Get request by ID",
    description="Retrieve a specific request by its ID",
    responses={
        status.HTTP_200_OK: {"description": "Request returned successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Request not found"},
    },
)
async def get_request_by_id(
    request_id: int,
    service: RequestServiceDep,
    cur_admin: CurrentAdminDep,
) -> Request:
    request = await service.get(request_id)
    return Request.model_validate(request)


@router.post(
    "",
    summary="Create a new request",
    description="Create a new request",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"description": "Request created successfully"},
    },
)
async def create_new_request(application: RequestCreate, service: RequestServiceDep) -> Request:
    request_model = RequestModel(**application.to_dict())
    request_created = await service.create(request_model)
    return Request.model_validate(request_created)


@router.delete(
    "/{request_id}",
    summary="Delete a request",
    description="Delete a request by its ID",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Request deleted successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Request not found"},
    },
)
async def delete_request_by_id(
    request_id: int,
    service: RequestServiceDep,
    cur_admin: CurrentAdminDep,
) -> None:
    await service.delete(request_id)


@router.patch(
    "/{request_id}",
    summary="Partially update a request",
    description="Partially update a request by its ID",
    responses={
        status.HTTP_200_OK: {"description": "Request updated successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Request not found"},
    },
)
async def update_request_by_id(
    request_id: int,
    request: RequestPartialUpdate,
    service: RequestServiceDep,
    cur_admin: CurrentAdminDep,
) -> Request:
    request_updated = await service.update(request_id, request.to_dict())
    return Request.model_validate(request_updated)
