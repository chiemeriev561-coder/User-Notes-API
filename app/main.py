from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from app.api.routes.notes import router as notes_router
from app.api.routes.auth import router as auth_router
from app.db import init_db

app = FastAPI(title="notes API")

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def root():
    return {"status": "ok"}

# Include routers
app.include_router(auth_router)
app.include_router(notes_router)
