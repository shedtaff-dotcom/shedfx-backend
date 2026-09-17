from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models._mixins import UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.effects_flow import EffectsFlow
    from app.models.song import Song


class SongFootswitch(UUIDPrimaryKeyMixin, Base):
    """Assigns an effects flow to one of a song's four footswitch slots."""

    __tablename__ = "song_footswitch"
    __table_args__ = (
        UniqueConstraint("song_id", "switch_slot"),
        CheckConstraint("switch_slot BETWEEN 1 AND 4", name="ck_song_footswitch_slot_range"),
    )

    song_id: Mapped[str] = mapped_column(String(36), ForeignKey("song.id", ondelete="CASCADE"))
    effects_flow_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("effects_flow.id", ondelete="CASCADE")
    )
    switch_slot: Mapped[int] = mapped_column(Integer)

    song: Mapped["Song"] = relationship(back_populates="footswitches")
    effects_flow: Mapped["EffectsFlow"] = relationship(back_populates="song_footswitches")
