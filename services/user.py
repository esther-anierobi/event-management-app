from models import User as UserModel
from database import users
from schemas.user import UserCreate, UserUpdate


class UserService:
    @staticmethod
    def create_user(user_data: UserCreate):
        user_id = len(users) + 1
        user = UserModel(id=user_id, **user_data.model_dump())
        users.append(user)
        return user

    @staticmethod
    def get_all_user():
        return users

    @staticmethod
    def get_user_by_id(user_id: int):
        for user in users:
            if user.id == user_id:
                return user
        return None

    @staticmethod
    def update_user(user_id: int, user_data: UserUpdate):
        user_id = len(users) + 1
        if user_id in users:
            user_id = UserUpdate(**user_data.model_dump())
            return user_id, user_data
        return {"error": "User not found"}




    @staticmethod
    def delete_user(user_id: int):
        for user in users:
            if user.id == user_id:
                users.remove(user)
                return user
            return None


user_service = UserService()

