from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from jose import jwt
from app.models.user_model import User
from app.schemas.auth_schema import TokenPayload
from fastapi import HTTPException, status
from datetime import datetime
from pydantic import ValidationError
from app.services.user_services import UserService
from fastapi import Depends





reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login",  # Resolves to /api/v1/auth/login
    scheme_name="JWT",
)

async def get_current_user(token: str = Depends(reusable_oauth2))-> User:
    try:
        payload = jwt.decode( token,settings.JWT_SECRET_KEY, settings.ALGORITHM)

        token_data = TokenPayload(**payload)
        if datetime.fromtimestamp(token_data.exp)< datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError,ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = await UserService.get_user_by_id(token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

## kraht wallah wach hada backend ya chkopii aah wech dani ntla3 university 
