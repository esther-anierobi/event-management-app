import uuid
from pydantic import BaseModel
from models import User as UserModel
from database import users
from schemas.user import UserCreate, UserUpdate


class UserService:
    @staticmethod
    def create_user(user_data: UserCreate):
        user_id = len(users) + 1
        user = UserModel(user_id, user_data.model_dump())
        return user

    @staticmethod
    def get_all_user():
        return users

    @staticmethod
    def get_user_by_id(user_id: int):
        for user in users:
            if user.id == user_id:
                return users.get(user_id)
        return None

    @staticmethod
    def update_user(user_id: int, user_data: UserUpdate):
        for user in users:
            if user.id == user_id:
                user_data.model_update(user_id, user_data.model_dump())
                return user
            return None

    @staticmethod
    def delete_user(user_id: int):
        for user in users:
            if user.id == user_id:
                users.remove(user)
                return user
            return None




