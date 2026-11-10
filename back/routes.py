from fastapi import APIRouter

# 
# Routes
# 

router = APIRouter(prefix="/api/notes", tags=["notes"])

@router.get("")
def list_notes():