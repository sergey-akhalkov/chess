from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import users_curd
from app.schemas.user_schemas import UserCreateSchema, UserSchema
from app.api.deps import get_db

router = APIRouter()


@router.get("/users")
async def get_users(skip: int = 0, limit: int = 10) -> int:
    return 1


@router.get("/users/me")
async def get_current_user() -> dict:
    return dict()


@router.post("/users/", response_model=UserSchema)
async def create_user(user: UserCreateSchema, 
                      db: Session = Depends(get_db)) -> UserSchema:
    db_user = await users_curd.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return users_curd.create_user(db=db, user=user)


@router.get("/users/{user_id}")
async def get_user_by_id(user_id: int) -> dict:
    return dict()


@router.get("/users/{user_id}/games")
async def get_user_games(user_id: int, skip: int = 0, limit: int = 10) -> list:
    return []
