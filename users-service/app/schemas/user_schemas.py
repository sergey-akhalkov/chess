from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    email: EmailStr


class UserCreateSchema(UserBaseSchema):
    password: str = None


class UserGetSchema(UserBaseSchema):
    id: int

    class Config:
        orm_mode = True
