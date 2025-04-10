from fastapi import APIRouter, HTTPException ,status
import pymongo.errors
from app.schemas.user_schema import UserAuth ,UserOut
from app.services.user_services import UserService
#from beanie.exceptions import DuplicateKeyError
import pymongo

user_router = APIRouter()



from pymongo.errors import DuplicateKeyError

@user_router.post("/create", summary="Create a new user",response_model=UserOut)
async def creat_user(data: UserAuth):
    try:
        user = await UserService.create_user(data)
        return user
    except DuplicateKeyError as e:
        # Parse the error details
        error_message = str(e)
        if "email_1" in error_message:
            detail = "Email already registered"
        elif "username_1" in error_message:
            detail = "Username already taken"
        else:
            detail = "Duplicate entry detected"
            
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )