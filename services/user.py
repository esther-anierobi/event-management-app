import uuid

from models import User as UserModel
from schemas.user import UserCreate



class UserService:
    @staticmethod
    def create_user(id: uuid.UUID, user: UserCreate):
        user = len(user) + 1
        user = UserModel(**user.model_dump())

    @staticmethod
    def get_all_user():
        pass
