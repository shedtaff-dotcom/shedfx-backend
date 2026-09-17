from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models._mixins import UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.setlist import Setlist
    from app.models.song import Song


class SetlistSong(UUIDPrimaryKeyMixin, Base):
    """Join row: a song's position within a setlist."""

    __tablename__ = "setlist_song"
    __table_args__ = (UniqueConstraint("setlist_id", "position"),)

    setlist_id: Mapped[str] = mapped_column(String(36), ForeignKey("setlist.id", ondelete="CASCADE"))
    song_id: Mapped[str] = mapped_column(String(36), ForeignKey("song.id", ondelete="CASCADE"))
    position: Mapped[int] = mapped_column(Integer)

    setlist: Mapped["Setlist"] = relationship(back_populates="songs")
    song: Mapped["Song"] = relationship(back_populates="setlist_entries")
