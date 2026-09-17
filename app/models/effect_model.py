from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models._mixins import UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.effect import Effect
    from app.models.model_library import ModelLibrary


class EffectModel(UUIDPrimaryKeyMixin, Base):
    """A loadable NAM capture / effect definition on disk."""

    __tablename__ = "effect_model"

    model_library_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("model_library.id", ondelete="RESTRICT")
    )
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str | None] = mapped_column(String)
    tone3000_id: Mapped[str | None] = mapped_column(String)
    file_path: Mapped[str | None] = mapped_column(String)

    model_library: Mapped["ModelLibrary"] = relationship(back_populates="effect_models")
    effects: Mapped[list["Effect"]] = relationship(back_populates="effect_model")
