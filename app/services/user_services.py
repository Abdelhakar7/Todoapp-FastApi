from app.schemas.user_schema import UserAuth
from app.models.user_model import User
from app.core.security import get_password_hash


class UserService:
    @staticmethod
    async def create_user(user: UserAuth):

        user_in = User(
            email =user.email,
            username = user.username,
            hashed_pwd = get_password_hash(user.password)

        )
        await user_in.save()
        return user_in
