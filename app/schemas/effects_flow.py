from pydantic import BaseModel

from app.schemas._base import ReadSchema


class EffectsFlowCreate(BaseModel):
    name: str
    description: str | None = None
    input_gain: float | None = None
    output_gain: float | None = None


class EffectsFlowUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    input_gain: float | None = None
    output_gain: float | None = None


class EffectsFlowRead(ReadSchema):
    name: str
    description: str | None
    input_gain: float | None
    output_gain: float | None
