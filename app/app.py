from fastapi import FastAPI 
from app.core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.models.user_model import User
import logging
import dns.resolver
from app.api.api_v1.router import router

app = FastAPI(

    title = settings.PROJECT_NAME,
    openapi_url = f"{settings.API_V1_STR}/openapi.json"
    
)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.on_event("startup")
async def app_init():
    """
    initialize crucial application services
    
    """
    
# Configure DNS resolver with Google's DNS
    dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
    dns.resolver.default_resolver.nameservers = ['8.8.8.8', '8.8.4.4']
    
    db_client= AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).TODOAPP
    await init_beanie(
        database =db_client,
        document_models =[
            User  
        ]
        )
    #await User.create_indexes()
   # await User.create_indexes()
    logger.info("runs succesfully ")

app.include_router(router ,prefix=settings.API_V1_STR)

