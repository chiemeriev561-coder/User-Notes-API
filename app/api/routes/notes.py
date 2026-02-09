from typing import List

from fastapi import APIRouter, HTTPException, status
import logging
from app.schemas.note import NoteCreate, NoteResponse
from app.services.notes_service import (
    create_note,
    get_all_notes,
    get_notes,
    delete_note
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.post("/", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def create(note: NoteCreate):
    try:
        logger.info(f"Creating note with title: {note.title}")
        result = create_note(note)
        logger.info(f"Successfully created note: {result}")
        return result
    except Exception as e:
        logger.error(f"Error creating note: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/", response_model=list[NoteResponse])
def list_notes():
    try:
        logger.info("Fetching all notes")
        result = get_all_notes()
        logger.info(f"Successfully fetched {len(result)} notes")
        return result
    except Exception as e:
        logger.error(f"Error fetching notes: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/{note_id}", response_model=NoteResponse)
def read(note_id: int):
    try:
        logger.info(f"Fetching note with id: {note_id}")
        note = get_notes(note_id)
        if not note:
            logger.warning(f"Note with id {note_id} not found")
            raise HTTPException(status_code=404, detail="Note not found")
        logger.info(f"Successfully fetched note: {note}")
        return note
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching note {note_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(note_id: int):
    try:
        logger.info(f"Deleting note with id: {note_id}")
        if not delete_note(note_id):
            logger.warning(f"Note with id {note_id} not found for deletion")
            raise HTTPException(status_code=404, detail="Note not found")
        logger.info(f"Successfully deleted note with id: {note_id}")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting note {note_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
