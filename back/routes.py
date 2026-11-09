from fastapi import APIRouter

# 
# Routes
# 

notes_router = APIRouter(prefix="/api/notes", tags=["notes"])

# @router.get("")
# def list_notes():
#     return get_notes()