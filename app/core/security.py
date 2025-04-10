from passlib.context import CryptContext
from typing import Union ,Any 
from datetime import datetime ,timedelta
from app.core.config import settings
from jose import jwt

pasword_context = CryptContext(schemes=["bcrypt"] ,deprecated="auto")


def create_access_token(subject: Union[str ,Any] ,expires_delta: int=None) -> str:

    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRATION)


    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

## aaay nti ragda haaanya w ana nkhamam fik 

def create_refresh_token(subject: Union[str ,Any] ,expires_delta: int=None) -> str:

    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=settings.REFRESH_ACCESS_TOKEN_EXPIRATION)


    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_REFRESH_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def get_password_hash(password: str) -> str:
    """
    Hashes the password using bcrypt
    """
    return pasword_context.hash(password)

def verify_password(password:str ,hashed_password:str) -> bool:
    """
    Verifies the password using bcrypt
    """
    return pasword_context.verify(password, hashed_password)