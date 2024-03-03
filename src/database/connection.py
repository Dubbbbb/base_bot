from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.settings import settings

__all__ = [
    "engine",
    "session_maker",
]


engine = create_engine(url=settings.DATABASE_URL.unicode_string())
session_maker = sessionmaker(bind=engine)
