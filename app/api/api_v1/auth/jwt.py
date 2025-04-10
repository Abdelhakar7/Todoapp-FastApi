from fastapi import APIRouter ,Depends
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from app.services.user_services import UserService
from app.core.security import create_access_token, create_refresh_token
from app.schemas.auth_schema import TokenSchema
from app.schemas.user_schema import UserOut
from app.api.api_v1.dependencies.user_deps import get_current_user
from app.models.user_model import User
from fastapi import Body
from jose import jwt
from app.schemas.auth_schema import TokenPayload
from app.core.config import settings
from pydantic import ValidationError

auth_router = APIRouter()

@auth_router.post("/login" ,summary="creat_access_and_refresh_token", response_model=TokenSchema)
async def login(form_data : OAuth2PasswordRequestForm = Depends(),)-> Any :
    user = await UserService.authenticate_user(email = form_data.username, password= form_data.password)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Invalid uname or password"
        )
    return{

        "access_token" : create_access_token(user.user_id),
        "refresh_token" : create_refresh_token(user.user_id),
    }

#yyayyyyaw roho hawloha 


@auth_router.post("/test_token" ,summary= "checkif the access token is valid" ,response_model=UserOut)
async def test_token(user: User = Depends(get_current_user)) -> UserOut:
    """
    This endpoint is used to test the access token
    """
    return user

@auth_router.post("/refresh_token" ,summary= "refresh the access token" ,response_model=TokenSchema)
async def refresh_token(refresh_token: str =Body(...)):
    try:
        payload = jwt.decode(refresh_token, settings.JWT_SECRET_REFRESH_KEY, settings.ALGORITHM)
        token_data = TokenPayload(**payload)
    except(jwt.JWTError, ValidationError):
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
    
    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id),
    }
#### maybe backend are the frnds we made along the way 


""" khawti had ahowa a othantikasion ??? ?""" 