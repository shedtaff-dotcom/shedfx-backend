from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models._mixins import UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.effect import Effect
    from app.models.effects_flow import EffectsFlow


class FootswitchMap(UUIDPrimaryKeyMixin, Base):
    """What a physical footswitch does while this flow is active."""

    __tablename__ = "footswitch_map"
    __table_args__ = (UniqueConstraint("effects_flow_id", "switch_number"),)

    effects_flow_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("effects_flow.id", ondelete="CASCADE")
    )
    switch_number: Mapped[int] = mapped_column(Integer)
    action: Mapped[str] = mapped_column(String)
    # Optional: not every action targets an effect (tap tempo, next preset, etc).
    target_effect_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("effect.id", ondelete="SET NULL")
    )

    effects_flow: Mapped["EffectsFlow"] = relationship(back_populates="footswitch_maps")
    target_effect: Mapped["Effect | None"] = relationship()
