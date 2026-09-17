from pydantic import BaseModel

from app.schemas._base import ReadSchema


class SetlistSongCreate(BaseModel):
    setlist_id: str
    song_id: str
    position: int


class SetlistSongUpdate(BaseModel):
    setlist_id: str | None = None
    song_id: str | None = None
    position: int | None = None


class SetlistSongRead(ReadSchema):
    setlist_id: str
    song_id: str
    position: int
