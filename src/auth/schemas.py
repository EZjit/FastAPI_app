from typing import Any

from fastapi_users import schemas
from pydantic import BaseModel, Json


class UserRead(schemas.BaseUser[int]):
    username: str
    role_id: int


class UserCreate(schemas.BaseUserCreate):
    username: str
    role_id: int


class UserUpdate(schemas.BaseUserUpdate):
    username: str


class RoleBase(BaseModel):
    name: str
    permissions: str


class RoleCreate(RoleBase):
    ...


class RoleRead(RoleBase):
    id: int

    class Config:
        orm_mode = True
