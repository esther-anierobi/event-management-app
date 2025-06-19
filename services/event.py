import uuid

from schemas.event import CreateEvent, UpdateEvent, DeleteEvent, GetEventById, GetAllEvents
from database import events
from models import Event as EventModel


class EventService:
    @staticmethod
    def get_all_events():
        return GetAllEvents()

    @staticmethod
    def get_event_by_id(event_id: uuid.UUID):
        return GetEventById(id=event_id)

    @staticmethod
    def create_event(event_details: CreateEvent):
        even_id = len(events) + 1
        event = EventModel(even_id, **event_details.model_dump())
        events.append(event)
        return event

    @staticmethod
    def update_event(event_id: uuid.UUID, event_details: UpdateEvent):
        for event in events:
            if event_details == event_details.model_load():
                event.id = event_id
                return event
            return None

    @staticmethod
    def delete_event(event_id: uuid.UUID):
        for event in events:
            if event_id == event.id:
                events.remove(event)
                return event
            return None


event_service = EventService()

