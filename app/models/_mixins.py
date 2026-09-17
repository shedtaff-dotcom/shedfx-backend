import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


def _new_id() -> str:
    return str(uuid.uuid4())


class UUIDPrimaryKeyMixin:
    """String UUID primary key, generated server-side on insert."""

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_new_id)
