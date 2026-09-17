from pydantic import BaseModel, Field

from app.schemas._base import ReadSchema


class SongFootswitchCreate(BaseModel):
    song_id: str
    effects_flow_id: str
    switch_slot: int = Field(ge=1, le=4)


class SongFootswitchUpdate(BaseModel):
    song_id: str | None = None
    effects_flow_id: str | None = None
    switch_slot: int | None = Field(default=None, ge=1, le=4)


class SongFootswitchRead(ReadSchema):
    song_id: str
    effects_flow_id: str
    switch_slot: int
