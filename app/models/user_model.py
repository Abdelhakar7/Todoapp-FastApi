from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from beanie import Document
from pydantic import Field, EmailStr

from pymongo import IndexModel  # Add this import

class User(Document):
    user_id: UUID = Field(default_factory=uuid4)
    username: str
    email: EmailStr
    hashed_pwd: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: Optional[bool] = None

    def __repr__(self) -> str:
        return f"<User {self.email}>"

    def __str__(self) -> str:
        return self.email

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, User) and self.email == other.email

    @property
    def create(self) -> datetime:
        return self.id.generation_time

    @classmethod
    async def by_email(cls, email: str) -> "User":
        return await cls.find_one(cls.email == email)

    class Settings:
        name = "users"
        indexes = [
            IndexModel([("username", 1)], unique=True),  # Use IndexModel
            IndexModel([("email", 1)], unique=True)      # Use IndexModel
        ]
