from fastapi import APIRouter

from app.api.endpoints import games_endpoint, users_endpoint, root_endpoint
from app.db import Base, engine

Base.metadata.create_all(bind=engine)

api_router = APIRouter()
api_router.include_router(games_endpoint.router, tags=["games"])
api_router.include_router(users_endpoint.router, tags=["users"])
api_router.include_router(root_endpoint.router, tags=["root"])
