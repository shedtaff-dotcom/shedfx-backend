from pydantic import BaseModel

from app.schemas._base import ReadSchema


class FootswitchMapCreate(BaseModel):
    effects_flow_id: str
    switch_number: int
    action: str
    target_effect_id: str | None = None


class FootswitchMapUpdate(BaseModel):
    effects_flow_id: str | None = None
    switch_number: int | None = None
    action: str | None = None
    target_effect_id: str | None = None


class FootswitchMapRead(ReadSchema):
    effects_flow_id: str
    switch_number: int
    action: str
    target_effect_id: str | None
