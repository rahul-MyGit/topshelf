from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from src.events.event_data import events
from src.events.schemas import Event, EventUpdateModel
from typing import List


event_router = APIRouter()

@event_router.get('/', response_model=List[Event])
async def getAllEvents() -> dict:
    return events


@event_router.post('/', status_code=status.HTTP_201_CREATED)
async def createEvents(event_data: Event) -> dict:
    new_event = event_data.model_dump()
    events.append(new_event)
    return new_event


@event_router.get('/{event_id}')
async def getEventById(event_id: int) -> dict:
    for event in events:
        if event['id'] == event_id:
            return event    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Event no t found')


@event_router.patch('/{event_id}')
async def updateEventById(event_id: int, updateData: EventUpdateModel) -> dict:
    for event in events:
        if event['id'] == event_id:
            event['name'] = updateData.name
            event['speaker'] = updateData.speaker
            event['publisher'] = updateData.publisher
            event['guests'] = updateData.guests
            event['language'] = updateData.language
            return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Event not found')


@event_router.delete('/{event_id}' , status_code=status.HTTP_204_NO_CONTENT)
async def deleteEventById(event_id: int):
    for event in events:
        if event['id'] == event_id:
            events.remove(event)
            return {}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Event not found')