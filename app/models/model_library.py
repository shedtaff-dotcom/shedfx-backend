from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models._mixins import UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.effect_model import EffectModel


class ModelLibrary(UUIDPrimaryKeyMixin, Base):
    """Where a set of effect models came from (e.g. a TONE3000 category)."""

    __tablename__ = "model_library"

    source: Mapped[str] = mapped_column(String)
    category: Mapped[str | None] = mapped_column(String)
    description: Mapped[str | None] = mapped_column(String)
    download_url: Mapped[str | None] = mapped_column(String)

    effect_models: Mapped[list["EffectModel"]] = relationship(back_populates="model_library")
