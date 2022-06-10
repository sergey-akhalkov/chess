from fastapi import FastAPI

from app.api.users_api import router as users_router
from app.database import async_engine, Base

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await async_engine.dispose()


app.include_router(users_router)
