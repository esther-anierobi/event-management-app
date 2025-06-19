import uuid
from http import HTTPStatus

from fastapi import APIRouter
from services.event import EventService
from database import events

event_router = APIRouter()


@event_router.get("/", status_code=HTTPStatus.OK)
def get_events():
    return {"events": EventService.get_all_events()}


@event_router.get("/{event_id}", status_code=HTTPStatus.OK)
def get_event_by_id(id: int):
    return {"event": EventService.get_event_by_id(events)}


@event_router.post("/", status_code=HTTPStatus.CREATED)
def create_event():
    return EventService.create_event(events)


@event_router.put("/", status_code=HTTPStatus.OK)
def update_event():
    return EventService.update_event(events)


@event_router.delete("/{event_id}", status_code=HTTPStatus.OK)
def delete_event():
    events.remove()
    return {"message": "event deleted"}

