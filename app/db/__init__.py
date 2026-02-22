from .session import engine
from .base import Base
from app.models.user import User
from app.models.note import Note

def init_db():
    Base.metadata.create_all(bind=engine)
