from pydantic import BaseModel

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