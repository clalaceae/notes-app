from pydantic import BaseModel, Field

class _NoteCreate(BaseModel):
    content: str
    tag_names: list[str] = Field(default_factory=list)

