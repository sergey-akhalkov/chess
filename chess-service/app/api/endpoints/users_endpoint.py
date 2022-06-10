from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user_schemas import UserCreateSchema, UserSchema
from app.models.user_model import UserModel

router = APIRouter()


@router.get("/users")
async def get_users(skip: int = 0, limit: int = 10) -> int:
    return 1


@router.get("/users/me")
async def get_current_user() -> dict:
    return dict()


@router.post("/users/", response_model=UserSchema)
async def create_user(user: UserCreateSchema) -> UserSchema:
    await UserModel.create(email=user.email, hashed_password=user.password)
    return users_curd.create_user(db=db, user=user)


@router.get("/users/{user_id}")
async def get_user_by_id(user_id: int) -> dict:
    return dict()
