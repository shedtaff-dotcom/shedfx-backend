from pydantic import BaseModel

from app.schemas._base import ReadSchema


class ModelLibraryCreate(BaseModel):
    source: str
    category: str | None = None
    description: str | None = None
    download_url: str | None = None


class ModelLibraryUpdate(BaseModel):
    source: str | None = None
    category: str | None = None
    description: str | None = None
    download_url: str | None = None


class ModelLibraryRead(ReadSchema):
    source: str
    category: str | None
    description: str | None
    download_url: str | None
