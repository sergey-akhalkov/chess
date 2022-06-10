from fastapi import FastAPI

from app.api.api import api_router
from app.database import async_db_session

app = FastAPI()


@app.on_event("startup")
async def startup():
    await async_db_session.init()
    await async_db_session.create_all()


app.include_router(api_router)
