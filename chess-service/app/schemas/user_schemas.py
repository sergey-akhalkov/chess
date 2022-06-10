from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    email: EmailStr


class UserCreateSchema(UserBaseSchema):
    password: str = None


class UserSchema(UserBaseSchema):
    id: int

    class Config:
        orm_mode = True
