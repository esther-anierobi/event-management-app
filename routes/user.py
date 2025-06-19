from http import HTTPStatus

from fastapi import APIRouter
from services.user import UserService
from database import users
from schemas.user import UserCreate, UserUpdate

user_router = APIRouter()


@user_router.get("/", status_code=HTTPStatus.CREATED)
def get_all_user():
    return UserService().get_all_user()


@user_router.post("/", status_code=HTTPStatus.CREATED)
def create_user(user_data: UserCreate):
    return UserService().create_user(user_data)


@user_router.get("/{user_id}", status_code=HTTPStatus.OK)
def get_user_by_id(user_id: int):
    return UserService().get_user_by_id(user_id)


@user_router.put("/", status_code=HTTPStatus.OK)
def update_user(user_id: int, user_data: UserUpdate):
    return UserService().update_user(user_id, user_data)


@user_router.delete("/{user_id}", status_code=HTTPStatus.OK)
def delete_user(user_id: int):
    return UserService.delete_user(user_id)

