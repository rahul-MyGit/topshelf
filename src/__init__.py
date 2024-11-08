from fastapi import FastAPI
from src.events.routes import event_router

version = 'v1'
app = FastAPI(
    title='topshelf',
    description='An event booking app which can perform CRUD operation',
    version = version
)

app.include_router(event_router, prefix=f'/api/{version}/event', tags=['event'])