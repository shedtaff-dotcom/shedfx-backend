from pydantic import BaseModel

from app.schemas._base import ReadSchema


class SongCreate(BaseModel):
    title: str
    artist: str | None = None
    key: str | None = None
    bpm: int | None = None
    lyrics_url: str | None = None
    tab_url: str | None = None
    notes: str | None = None


class SongUpdate(BaseModel):
    title: str | None = None
    artist: str | None = None
    key: str | None = None
    bpm: int | None = None
    lyrics_url: str | None = None
    tab_url: str | None = None
    notes: str | None = None


class SongRead(ReadSchema):
    title: str
    artist: str | None
    key: str | None
    bpm: int | None
    lyrics_url: str | None
    tab_url: str | None
    notes: str | None
