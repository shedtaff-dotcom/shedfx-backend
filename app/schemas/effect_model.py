from pydantic import BaseModel

from app.schemas._base import ReadSchema


class EffectModelCreate(BaseModel):
    model_library_id: str
    name: str
    type: str | None = None
    tone3000_id: str | None = None
    file_path: str | None = None


class EffectModelUpdate(BaseModel):
    model_library_id: str | None = None
    name: str | None = None
    type: str | None = None
    tone3000_id: str | None = None
    file_path: str | None = None


class EffectModelRead(ReadSchema):
    model_library_id: str
    name: str
    type: str | None
    tone3000_id: str | None
    file_path: str | None
