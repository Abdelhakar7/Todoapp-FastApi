from fastapi import APIRouter, HTTPException ,status
import pymongo.errors
from app.schemas.user_schema import UserAuth
from app.services.user_services import UserService
#from beanie.exceptions import DuplicateKeyError
import pymongo

user_router = APIRouter()



@user_router.post("/create",summary="Create a new user")
async def creat_user(data: UserAuth):
    """
    Create a new user.
    """
    try:
        user = await UserService.create_user(data)
        return {"message": "User created successfully", "user": user}
    except pymongo.errors.DuplicateKeyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))