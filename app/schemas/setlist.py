from pydantic import BaseModel

from app.schemas._base import ReadSchema


class SetlistCreate(BaseModel):
    name: str
    gig_date: str | None = None
    venue: str | None = None
    notes: str | None = None


class SetlistUpdate(BaseModel):
    name: str | None = None
    gig_date: str | None = None
    venue: str | None = None
    notes: str | None = None


class SetlistRead(ReadSchema):
    name: str
    gig_date: str | None
    venue: str | None
    notes: str | None
