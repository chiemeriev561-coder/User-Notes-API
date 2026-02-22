import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Use SQLite by default for development
USE_SQLITE = os.getenv("USE_SQLITE", "true").lower() == "true"

if USE_SQLITE:
    # SQLite configuration for local development
    SQLITE_DATABASE_URL = "sqlite:///./notes.db"
    engine = create_engine(
        SQLITE_DATABASE_URL, 
        connect_args={"check_same_thread": False}
    )
else:
    # PostgreSQL connection configuration
    DATABASE_USER = os.getenv("DB_USER", "postgres")
    DATABASE_PASSWORD = os.getenv("DB_PASSWORD", "password")
    DATABASE_HOST = os.getenv("DB_HOST", "localhost")
    DATABASE_PORT = os.getenv("DB_PORT", "5432")
    DATABASE_NAME = os.getenv("DB_NAME", "notes_db")

    DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

    engine = create_engine(
        DATABASE_URL,
        pool_size=20,  # Increase connection pool
        max_overflow=40,  # Allow overflow connections
        pool_pre_ping=True  # Check connection health
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
