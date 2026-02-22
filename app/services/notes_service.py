from typing import List
from sqlalchemy.orm import Session
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteResponse

def create_note(db: Session, note: NoteCreate, user_id: int) -> NoteResponse:
    db_note = Note(
        title=note.title,
        content=note.content,
        user_id=user_id
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_all_notes(db: Session, user_id: int) -> List[NoteResponse]:
    return db.query(Note).filter(Note.user_id == user_id).all()

def get_notes(db: Session, note_id: int, user_id: int) -> NoteResponse | None:
    return db.query(Note).filter(Note.id == note_id, Note.user_id == user_id).first()

def delete_note(db: Session, note_id: int, user_id: int) -> bool:
    note = db.query(Note).filter(Note.id == note_id, Note.user_id == user_id).first()
    if note:
        db.delete(note)
        db.commit()
        return True
    return False
