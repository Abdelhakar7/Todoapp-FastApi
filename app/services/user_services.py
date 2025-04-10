from app.schemas.user_schema import UserAuth
from app.models.user_model import User
from app.core.security import get_password_hash
from typing import Optional
from app.core.security import verify_password ,get_password_hash
from uuid import UUID

class UserService:
    @staticmethod
    async def create_user(user: UserAuth):

        user_in = User(
            email =user.email,
            username = user.username,
            hashed_pwd = get_password_hash(user.password)

        )
        await user_in.insert()
        return user_in
    @staticmethod
    async def authenticate_user(email: str, password: str) -> Optional[User]:
        user = await UserService.get_user_by_email(email=email)
        if not user:
            return None
        if not verify_password(password = password, hashed_password = user.hashed_pwd):
            return None
        return user
    @staticmethod

    async def get_user_by_email(email: str) -> Optional[User]:

       user = await User.find_one(User.email == email)
       return user
    @staticmethod

    async def get_user_by_id(id: UUID) -> Optional[User]:

       user = await User.find_one(User.user_id == id)
       return user