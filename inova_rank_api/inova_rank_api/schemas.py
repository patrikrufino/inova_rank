from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class FilterPage(BaseModel):
    offset: int = 0
    limit: int = 100


class CategoryIn(BaseModel):
    name: str


class CategoryOut(BaseModel):
    id: int
    name: str


class CategoriesList(BaseModel):
    categories: list[CategoryOut]


class IdeaIn(BaseModel):
    author_id: int
    title: str
    content: str
    category_id: int


class IdeaOut(BaseModel):
    id: int
    author: UserPublic
    title: str
    content: str
    category: CategoryOut
    num_genius: int
    num_stupid: int
    created_at: datetime


class IdeaList(BaseModel):
    ideas: list[IdeaOut]
