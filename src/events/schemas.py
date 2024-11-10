from pydantic import BaseModel
import uuid;
from datetime import datetime

class Event(BaseModel):
    uid: uuid.UUID
    name: str
    speaker: str
    publisher: str
    event_date: str
    guests: int
    ticket: int
    language: str
    created_at: datetime 
    updated_at: datetime


class EventcreateModel(BaseModel):
    name: str
    speaker: str
    publisher: str
    event_date: str
    guests: int
    ticket: int
    language: str


class EventUpdateModel(BaseModel):
    name: str
    speaker: str
    publisher: str
    guests: int
    language: str