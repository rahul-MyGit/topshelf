from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime, date
import uuid

class Event(SQLModel, table=True):
    __tablename__ = 'events'

    uid: uuid.UUID = Field(
        sa_column= Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    name: str
    speaker: str
    publisher: str
    event_date: date
    guests: int
    ticket: int
    language: str
    created_at: datetime = Field(sa_column= Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime =  Field(sa_column= Column(pg.TIMESTAMP, default=datetime.now))


    # TODO: WORKING ???
    def __repr__(self):
        return f"<Book {self.title} >"
