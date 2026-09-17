from pydantic import BaseModel

from app.schemas._base import ReadSchema


class LedDisplayCreate(BaseModel):
    effects_flow_id: str
    label: str | None = None
    colour: str | None = None
    brightness: int | None = None


class LedDisplayUpdate(BaseModel):
    effects_flow_id: str | None = None
    label: str | None = None
    colour: str | None = None
    brightness: int | None = None


class LedDisplayRead(ReadSchema):
    effects_flow_id: str
    label: str | None
    colour: str | None
    brightness: int | None
