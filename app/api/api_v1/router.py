from fastapi import APIRouter
from app.api.api_v1.handlers import users_handler
router = APIRouter()
router.include_router(users_handler.user_router, prefix="/users", tags=["users"])
