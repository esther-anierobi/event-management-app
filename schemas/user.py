from typing import Annotated
from uuid import UUID

from fastapi import Form
from pydantic import  BaseModel


class UserBase(BaseModel):
    name: Annotated[str, Form()]
    email: Annotated[str, Form()]


class UserCreate(UserBase):
    is_active: bool = True


class UserUpdate(UserBase):
    is_active: bool = False


class User(UserBase):
    id: UUID