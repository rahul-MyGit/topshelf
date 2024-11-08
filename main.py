from fastapi import FastAPI
from typing import List
from pydantic import BaseClass


events = [
    {
        'id': 1,
        'name': 'Tech talk on golang',
        'speaker': 'Ram',
        'publisher': '1xDevs',
        'event_date': '2024-03-02',
        'guests': 10,
        'lanuage': 'Hindi'
    },
    {
        'id': 2,
        'name': 'Tech talk on DSA',
        'speaker': 'Vikas',
        'publisher': '1xDevs',
        'event_date': '2024-12-02',
        'guests': 1,
        'lanuage': 'English'
    },
    {
        'id': 3,
        'name': 'Tech talk on TypeScript',
        'speaker': 'harkuz',
        'publisher': '100xDevs',
        'event_date': '2024-11-12',
        'guests': 0,
        'lanuage': 'English'
    },
    {
        'id': 4,
        'name': 'Tech talk on FastAPI',
        'speaker': 'Kon hi hoga',
        'publisher': '100xDevs',
        'event_date': '2024-11-07',
        'guests': 1,
        'lanuage': 'English'
    },
    {
        'id': 5,
        'name': 'Tech talk on nothing',
        'speaker': 'nothing',
        'publisher': '10xCoffee',
        'event_date': '2024-11-18',
        'guests': 30,
        'lanuage': ':any'
    }
]

class Event(BaseClass):
    id: int
    name: str
    speaker: str
    publisher: str
    event_date: str
    guest: int
    language: str


app = FastAPI()

@app.get('/event', response_model=List[Event])
async def getAllEvents():
    return events

@app.post('/event')
async def createEvents(data):
    pass

@app.post('/event/{event_id}')
async def getEventById(event_id: str):
    pass

@app.delete('/event/')
async def deleteEventById(event_id: str):
    pass