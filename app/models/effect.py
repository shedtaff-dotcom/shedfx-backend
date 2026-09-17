from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models._mixins import UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.effect_model import EffectModel
    from app.models.effect_params import EffectParams
    from app.models.effects_flow import EffectsFlow


class Effect(UUIDPrimaryKeyMixin, Base):
    """One slot in a flow's signal chain, instantiating an EFFECT_MODEL."""

    __tablename__ = "effect"
    __table_args__ = (UniqueConstraint("effects_flow_id", "chain_position"),)

    effects_flow_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("effects_flow.id", ondelete="CASCADE")
    )
    effect_model_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("effect_model.id", ondelete="RESTRICT")
    )
    chain_position: Mapped[int] = mapped_column(Integer)
    enabled: Mapped[bool] = mapped_column(Boolean, default=True)

    effects_flow: Mapped["EffectsFlow"] = relationship(back_populates="effects")
    effect_model: Mapped["EffectModel"] = relationship(back_populates="effects")
    params: Mapped[list["EffectParams"]] = relationship(
        back_populates="effect", cascade="all, delete-orphan"
    )
