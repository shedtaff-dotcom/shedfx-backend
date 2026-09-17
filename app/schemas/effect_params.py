from pydantic import BaseModel

from app.schemas._base import ReadSchema


class EffectParamsCreate(BaseModel):
    effect_id: str
    param_name: str
    value: float | None = None
    min: float | None = None
    max: float | None = None


class EffectParamsUpdate(BaseModel):
    effect_id: str | None = None
    param_name: str | None = None
    value: float | None = None
    min: float | None = None
    max: float | None = None


class EffectParamsRead(ReadSchema):
    effect_id: str
    param_name: str
    value: float | None
    min: float | None
    max: float | None
