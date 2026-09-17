from pydantic import BaseModel

from app.schemas._base import ReadSchema


class EffectCreate(BaseModel):
    effects_flow_id: str
    effect_model_id: str
    chain_position: int
    enabled: bool = True


class EffectUpdate(BaseModel):
    effects_flow_id: str | None = None
    effect_model_id: str | None = None
    chain_position: int | None = None
    enabled: bool | None = None


class EffectRead(ReadSchema):
    effects_flow_id: str
    effect_model_id: str
    chain_position: int
    enabled: bool
