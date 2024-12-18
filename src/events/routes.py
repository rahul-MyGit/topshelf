from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from src.events.schemas import Event, EventUpdateModel, EventcreateModel
from typing import List
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from src.events.service import EventService
from src.auth.dependencies import TokenBearer


event_router = APIRouter()
event_service = EventService()
access_token_bearer = TokenBearer()


@event_router.get('/', response_model=List[Event])
async def get_all_events(session: AsyncSession = Depends(get_session), user_data: dict = Depends(access_token_bearer)):
    events = await event_service.get_all_events(session)
    print(user_data)
    return events


@event_router.post('/', status_code=status.HTTP_201_CREATED, response_model=Event)
async def createEvents(event_data: EventcreateModel, session: AsyncSession = Depends(get_session), user_data: dict = Depends(access_token_bearer)) -> dict:
    new_event = await event_service.create_event(event_data, session)
    return new_event


@event_router.get('/{event_uid}', response_model=Event)
async def getEventById(event_uid: str, session: AsyncSession = Depends(get_session), user_data: dict = Depends(access_token_bearer)) -> dict:
    event = await event_service.get_event(event_uid, session)

    if event:
        return event
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Event no t found')


@event_router.patch('/{event_uid}', response_model=Event)
async def updateEventById(event_uid: str, event_data: EventUpdateModel, session: AsyncSession = Depends(get_session), user_data: dict = Depends(access_token_bearer)) -> dict:
    updated_event = await event_service.update_event(event_uid, event_data, session)
    
    if updated_event:
        return updated_event
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Event not found')


@event_router.delete('/{event_uid}' , status_code=status.HTTP_204_NO_CONTENT)
async def deleteEventById(event_uid: str, session:AsyncSession = Depends(get_session), user_data: dict = Depends(access_token_bearer)):
    delete_event = await event_service.delete_event(event_uid, session)

    if delete_event:
        return None
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Event not found')