from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./test.db"
    secret_key: str = "super-secret"
    algorithm: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()