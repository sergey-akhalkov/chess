from http import HTTPStatus
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user_schemas import UserCreateSchema, UserGetSchema
from app.models.user_model import UserModel
from app.crud import users_curd
from app.database import get_db


router = APIRouter()


# TODO - protect this endpoint so it can be called only by super user
@router.get("/users", response_model=list[UserGetSchema])
async def get_users(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return 1


@router.get("/users/me", response_model=UserGetSchema)
async def get_current_user(db: AsyncSession = Depends(get_db)):
    return dict()


# TODO - confirm user email 
@router.post("/users/", response_model=int)
async def create_user(user: UserCreateSchema, db: AsyncSession = Depends(get_db)):
    existing_user = await users_curd.get_by_email(db, user.email)
    if existing_user:
        raise HTTPException(HTTPStatus.BAD_REQUEST, "User with specified email already exists")
    user = UserModel(email=user.email, hashed_password=user.password)
    await users_curd.create(db, user)
    return user.id


# TODO - protect this endpoint so it can be called only by super user
@router.get("/users/{user_id}", response_model=UserGetSchema) 
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await users_curd.get_by_id(db, user_id)
    if not user:
        raise HTTPException(HTTPStatus.BAD_REQUEST, "User with specified id does not exist")
    return user
