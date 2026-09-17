"""Generic CRUD router factory.

Every entity router is the same five endpoints over a different model and
schema trio, so build them here. Entity-specific behaviour (nested reads,
validation beyond the schema, etc.) belongs in the entity's own router file
when it's needed — this is scaffolding, not the final API design.

NOTE: no ``from __future__ import annotations`` here — FastAPI needs the real
schema classes as annotations at decoration time.
"""

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import Base, get_db


def _commit_or_409(db: Session) -> None:
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status.HTTP_409_CONFLICT, detail=str(exc.orig)) from exc


def make_crud_router(
    *,
    model: type[Base],
    create_schema: type[BaseModel],
    update_schema: type[BaseModel],
    read_schema: type[BaseModel],
    prefix: str,
    tag: str,
) -> APIRouter:
    router = APIRouter(prefix=prefix, tags=[tag])

    def _get_or_404(db: Session, item_id: str) -> Any:
        obj = db.get(model, item_id)
        if obj is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"{tag} {item_id} not found")
        return obj

    @router.get("", response_model=list[read_schema])
    def list_items(db: Session = Depends(get_db)):
        return db.scalars(select(model)).all()

    @router.get("/{item_id}", response_model=read_schema)
    def get_item(item_id: str, db: Session = Depends(get_db)):
        return _get_or_404(db, item_id)

    @router.post("", response_model=read_schema, status_code=status.HTTP_201_CREATED)
    def create_item(payload: create_schema, db: Session = Depends(get_db)):
        obj = model(**payload.model_dump())
        db.add(obj)
        _commit_or_409(db)
        db.refresh(obj)
        return obj

    @router.put("/{item_id}", response_model=read_schema)
    def update_item(item_id: str, payload: update_schema, db: Session = Depends(get_db)):
        obj = _get_or_404(db, item_id)
        for field, value in payload.model_dump(exclude_unset=True).items():
            setattr(obj, field, value)
        _commit_or_409(db)
        db.refresh(obj)
        return obj

    @router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_item(item_id: str, db: Session = Depends(get_db)) -> None:
        obj = _get_or_404(db, item_id)
        db.delete(obj)
        _commit_or_409(db)

    return router
