from fastapi import APIRouter, Query, status

from src.auth.security.dependencies import CurrentAdminDep
from src.events.dependencies import EventServiceDep
from src.events.models import EventModel
from src.events.schemas import Event, EventCreate, EventList, EventPartialUpdate, EventUpdate

router = APIRouter(prefix="/events", tags=["Events"])


@router.get(
    "",
    summary="List all events",
    description="Retrieve a list of all events",
    responses={
        status.HTTP_200_OK: {"description": "List of all events returned successfully"},
    },
)
async def get_all_events(
    service: EventServiceDep,
    actual: bool = Query(False, description="Return only events that have not passed"),
) -> EventList:
    events = await service.get_events(actual)
    return EventList.from_orm_list(events)


@router.get(
    "/{event_id}",
    summary="Get event by ID",
    description="Retrieve a specific event by its ID",
    responses={
        status.HTTP_200_OK: {"description": "Event returned successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Event not found"},
    },
)
async def get_event_by_id(event_id: int, service: EventServiceDep) -> Event:
    event = await service.get(event_id)
    return Event.model_validate(event)


@router.post(
    "",
    summary="Create a new event",
    description="Create a new event",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"description": "Event created successfully"},
    },
)
async def create_new_event(
    event: EventCreate,
    service: EventServiceDep,
    cur_admin: CurrentAdminDep,
) -> Event:
    event_model = EventModel(**event.to_dict())
    event_created = await service.create(event_model)
    return Event.model_validate(event_created)


@router.delete(
    "/{event_id}",
    summary="Delete an event",
    description="Delete an event by its ID",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Event deleted successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Event not found"},
    },
)
async def delete_event_by_id(
    event_id: int,
    service: EventServiceDep,
    cur_admin: CurrentAdminDep,
) -> None:
    await service.delete(event_id)


@router.put(
    "/{event_id}",
    summary="Update an event",
    description="Update an event by its ID",
    responses={
        status.HTTP_200_OK: {"description": "Event updated successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Event not found"},
    },
)
async def update_event_by_id(
    event_id: int,
    event: EventUpdate,
    service: EventServiceDep,
    cur_admin: CurrentAdminDep,
) -> Event:
    event_updated = await service.update(event_id, event.to_dict())
    return Event.model_validate(event_updated)


@router.patch(
    "/{event_id}",
    summary="Partially update an event",
    description="Partially update an event by its ID",
    responses={
        status.HTTP_200_OK: {"description": "Event partially updated successfully"},
        status.HTTP_404_NOT_FOUND: {"description": "Event not found"},
    },
)
async def partial_update_event_by_id(
    event_id: int,
    event: EventPartialUpdate,
    service: EventServiceDep,
    cur_admin: CurrentAdminDep,
) -> Event:
    event_updated = await service.update(event_id, event.to_dict())
    return Event.model_validate(event_updated)
