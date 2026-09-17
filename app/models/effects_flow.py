from typing import TYPE_CHECKING

from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models._mixins import UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.effect import Effect
    from app.models.footswitch_map import FootswitchMap
    from app.models.led_display import LedDisplay
    from app.models.song_footswitch import SongFootswitch


class EffectsFlow(UUIDPrimaryKeyMixin, Base):
    """A preset: an ordered chain of effects plus its display and switch map."""

    __tablename__ = "effects_flow"

    name: Mapped[str] = mapped_column(String)
    description: Mapped[str | None] = mapped_column(String)
    input_gain: Mapped[float | None] = mapped_column(Float)
    output_gain: Mapped[float | None] = mapped_column(Float)

    effects: Mapped[list["Effect"]] = relationship(
        back_populates="effects_flow",
        cascade="all, delete-orphan",
        order_by="Effect.chain_position",
    )
    led_display: Mapped["LedDisplay | None"] = relationship(
        back_populates="effects_flow", cascade="all, delete-orphan", uselist=False
    )
    footswitch_maps: Mapped[list["FootswitchMap"]] = relationship(
        back_populates="effects_flow",
        cascade="all, delete-orphan",
        order_by="FootswitchMap.switch_number",
    )
    song_footswitches: Mapped[list["SongFootswitch"]] = relationship(
        back_populates="effects_flow", cascade="all, delete-orphan"
    )
