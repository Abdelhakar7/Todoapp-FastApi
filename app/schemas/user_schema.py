from pydantic import BaseModel, Field, EmailStr

class UserAuth(BaseModel):
    """
    User authentication schema
    """
    email: EmailStr = Field(..., description="user email")
    username: str = Field(..., min_length=5,max_length=25,description="Username of the user")
    password: str = Field(..., min_length= 5, max_length=25 , description="Password of the user")