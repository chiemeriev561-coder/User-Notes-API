from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from app.api.routes.notes import router
from app.db import init_db

app = FastAPI(title="notes API")

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def root():
    return {"status": "ok"}

# `notes` is an APIRouter exported from `app.api.routes`
app.include_router(router)
