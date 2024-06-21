from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str
    email: EmailStr
    password: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr


class UserDB(UserSchema):
    id: int
