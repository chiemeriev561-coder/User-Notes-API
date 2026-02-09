from typing import List
from app.schemas.note import NoteCreate, NoteResponse

_notes = []
_id_counter = 1

def create_note(note: NoteCreate) -> NoteResponse:
    global _id_counter
    
    new_note = NoteResponse(
        id=_id_counter,
        title=note.title,
        content=note.content
    )
    
    _notes.append(new_note)
    _id_counter += 1
    
    return new_note

def get_all_notes() -> List[NoteResponse]:
    return _notes

def get_notes(note_id: int) -> NoteResponse | None:
    for note in _notes:
        if note.id == note_id:
            return note
    return None

def delete_note(note_id: int) -> bool:
    global _notes
    for note in _notes:
        if note.id == note_id:
            _notes.remove(note)
            return True
    return False
