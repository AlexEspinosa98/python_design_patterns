from sqlalchemy import create_engine, MetaData

from .config import settings

engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})
metadata = MetaData()
