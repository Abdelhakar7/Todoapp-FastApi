from passlib.context import CryptContext

pasword_context = CryptContext(schemes=["bcrypt"] ,deprecated="auto")

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