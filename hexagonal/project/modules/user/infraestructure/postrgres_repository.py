from ..domain.models import User
from ..domain.repository import UserRepository
from sqlalchemy import Table, Column, Integer, String, select
from core.database import metadata

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, unique=True, nullable=False),
    Column("email", String, nullable=False),
    Column("password_hash", String, nullable=False)
)


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, engine):
        self.engine = engine
        metadata.create_all(engine)

    def create_user(self, user: User):
        with self.engine.begin() as conn:
            conn.execute(
                users_table.insert().values(
                    id=user.id,
                    username=user.username,
                    email=user.email,
                    password_hash=user.password_hash
                )
            )

    def get_by_username(self, username: str):
        with self.engine.connect() as conn:
            result = conn.execute(
                select(users_table).where(users_table.c.username == username)
            ).first()
            if result:
                return User(**result._mapping)
            return None
