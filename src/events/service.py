from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import EventcreateModel, EventUpdateModel
from sqlmodel import select, desc
from .models import Event

class EventService:
    async def get_all_events(self, session: AsyncSession):
        statement = select(Event).order_by(desc(Event.created_at))

        res = await session.exec(statement)

        return res.all()

    async def get_event(self, event_uid: str,session: AsyncSession):
        statement = select(Event).where(Event.uid == event_uid)

        res = await session.exec(statement)

        event =  res.first()

        return event if event is not None else None

    async def create_event(self, event_data: EventcreateModel, session:AsyncSession):
        event_data_in_dict = event_data.model_dump()

        new_event = Event(
            **event_data_in_dict
        )

        session.add(new_event)
        await session.commit()

        return new_event()


    async def update_event(self, event_uid: str, event_data: EventUpdateModel, session:AsyncSession):
        event_to_update = self.get_event(event_uid, session)

        if event_to_update is not None:
            event_update_data_in_dict = event_data.model_dump()

            for k , v in event_update_data_in_dict.items():
                setattr(event_to_update, k , v)

            await session.commit()
            return event_to_update
        else:
            return None

    async def delete_event(self, event_uid: str,session: AsyncSession):
        
        event_to_delete = self.get_event(event_uid, session)

        if event_to_delete is not None:
            await session.delete(event_to_delete)

            await session.commit()
            return {}
        else:
            return None


