from app.db.base import Base
from app.models.note import Note

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    from app.db.session import engine
    create_tables()
    print("Database tables created successfully!")
