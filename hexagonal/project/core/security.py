from passlib.context import CryptContext
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hash a password using a secure hashing algorithm.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_token(data: dict, secret_key: str = "your_secret_key", algorithm: str = "HS256") -> str:
    """
    Create a JWT token with the given data.
    """
    return jwt.encode(data, secret_key, algorithm=algorithm)
