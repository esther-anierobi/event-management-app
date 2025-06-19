import uuid
from typing import Annotated, Optional, List
from pydantic import BaseModel, Field
from fastapi import Form


class Event(BaseModel):
    name: Annotated[str, Form()]
    title: Annotated[str, Form()]


class CreateEvent(Event):
    is_open: bool = True


class UpdateEvent(Event):
    is_open: bool = True


class DeleteEvent(Event):
    is_open: bool = True


class GetAllEvents(BaseModel):
    events: List[Event]


class GetEventById(BaseModel):
    id: uuid.UUID


class Events(Event):
    id: Annotated[uuid.UUID, None]




