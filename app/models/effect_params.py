from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models._mixins import UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.effect import Effect


class EffectParams(UUIDPrimaryKeyMixin, Base):
    """A single named parameter value on an effect instance."""

    __tablename__ = "effect_params"
    __table_args__ = (UniqueConstraint("effect_id", "param_name"),)

    effect_id: Mapped[str] = mapped_column(String(36), ForeignKey("effect.id", ondelete="CASCADE"))
    param_name: Mapped[str] = mapped_column(String)
    value: Mapped[float | None] = mapped_column(Float)
    min: Mapped[float | None] = mapped_column(Float)
    max: Mapped[float | None] = mapped_column(Float)

    effect: Mapped["Effect"] = relationship(back_populates="params")
