from fastapi import FastAPI
from src.events.routes import event_router
from src.db.main import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f'server has started')
    await init_db()

    yield
    print(f'server has been stop')

version = 'v1'
app = FastAPI(
    title='topshelf',
    description='An event booking app which can perform CRUD operation',
    version = version,
    lifespan=life_span
)

app.include_router(event_router, prefix=f'/api/{version}/event', tags=['event'])