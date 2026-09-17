from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models._mixins import UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.effects_flow import EffectsFlow


class LedDisplay(UUIDPrimaryKeyMixin, Base):
    """One-to-one with EFFECTS_FLOW: what the LED shows when this flow is active."""

    __tablename__ = "led_display"

    effects_flow_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("effects_flow.id", ondelete="CASCADE"), unique=True
    )
    label: Mapped[str | None] = mapped_column(String)
    colour: Mapped[str | None] = mapped_column(String)
    brightness: Mapped[int | None] = mapped_column(Integer)

    effects_flow: Mapped["EffectsFlow"] = relationship(back_populates="led_display")
