import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# PostgreSQL connection configuration
DATABASE_USER = os.getenv("DB_USER", "postgres")
DATABASE_PASSWORD = os.getenv("DB_PASSWORD", "password")
DATABASE_HOST = os.getenv("DB_HOST", "localhost")
DATABASE_PORT = os.getenv("DB_PORT", "5432")
DATABASE_NAME = os.getenv("DB_NAME", "notes_db")

DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=40,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
