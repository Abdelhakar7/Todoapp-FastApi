from fastapi import APIRouter
from app.api.api_v1.handlers import users_handler
from app.api.api_v1.auth.jwt import auth_router 
router = APIRouter()
router.include_router(users_handler.user_router, prefix="/users", tags=["users"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])