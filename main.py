from fastapi import FastAPI, status
from fastapi import HTTPException
from typing import List
from pydantic import BaseModel


events = [
    {
        'id': 1,
        'name': 'Tech talk on golang',
        'speaker': 'Ram',
        'publisher': '1xDevs',
        'event_date': '2024-03-02',
        'guests': 10,
        'language': 'Hindi'
    },
    {
        'id': 2,
        'name': 'Tech talk on DSA',
        'speaker': 'Vikas',
        'publisher': '1xDevs',
        'event_date': '2024-12-02',
        'guests': 1,
        'language': 'English'
    },
    {
        'id': 3,
        'name': 'Tech talk on TypeScript',
        'speaker': 'harkuz',
        'publisher': '100xDevs',
        'event_date': '2024-11-12',
        'guests': 0,
        'language': 'English'
    },
    {
        'id': 4,
        'name': 'Tech talk on FastAPI',
        'speaker': 'Kon hi hoga',
        'publisher': '100xDevs',
        'event_date': '2024-11-07',
        'guests': 1,
        'language': 'English'
    },
    {
        'id': 5,
        'name': 'Tech talk on nothing',
        'speaker': 'nothing',
        'publisher': '10xCoffee',
        'event_date': '2024-11-18',
        'guests': 30,
        'language': ':any'
    }
]

class Event(BaseModel):
    id: int
    name: str
    speaker: str
    publisher: str
    event_date: str
    guests: int
    language: str

class EventUpdateModel(BaseModel):
    name: str
    speaker: str
    publisher: str
    guests: int
    language: str

app = FastAPI()

@app.get('/event', response_model=List[Event])
async def getAllEvents() -> dict:
    return events


@app.post('/event', status_code=status.HTTP_201_CREATED)
async def createEvents(event_data: Event) -> dict:
    new_event = event_data.model_dump()
    events.append(new_event)
    return new_event


@app.get('/event/{event_id}')
async def getEventById(event_id: int) -> dict:
    for event in events:
        if event['id'] == event_id:
            return event    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Event no t found')


@app.patch('/event/{event_id}')
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


@app.delete('/event/{event_id}' , status_code=status.HTTP_204_NO_CONTENT)
async def deleteEventById(event_id: int):
    for event in events:
        if event['id'] == event_id:
            events.remove(event)
            return {}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Event not found')