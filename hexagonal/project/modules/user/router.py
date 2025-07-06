""" router for module user """
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from infraestructure.postrgres_repository import SQLAlchemyUserRepository
from sqlalchemy.engine import Engine
from application.user_case import RegisterUser, LoginUser


router = APIRouter(prefix="/user", tags=["user"])


class RegisterRequest(BaseModel):
    username: str
    password: str
    email: str


class LoginRequest(BaseModel):
    email: str
    password: str


def get_repo(engine: Engine) -> SQLAlchemyUserRepository:
    """ get user repository """
    return SQLAlchemyUserRepository(engine)


@router.post("/register")
async def register(request: RegisterRequest, repo: SQLAlchemyUserRepository= Depends(get_repo)) -> dict:
    """ register a new user """
    use_case = RegisterUser(repo)
    await use_case.execute(request.username, request.password, request.email)
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(request: LoginRequest, repo: SQLAlchemyUserRepository = Depends(get_repo)) -> dict:
    """ login an existing user """
    try:
        use_case = LoginUser(repo)
        token = await use_case.execute(request.email, request.password)
        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid credentials")
