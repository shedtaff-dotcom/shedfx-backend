from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models._mixins import UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.setlist_song import SetlistSong
    from app.models.song_footswitch import SongFootswitch


class Song(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "song"

    title: Mapped[str] = mapped_column(String)
    artist: Mapped[str | None] = mapped_column(String)
    key: Mapped[str | None] = mapped_column(String)
    bpm: Mapped[int | None] = mapped_column(Integer)
    lyrics_url: Mapped[str | None] = mapped_column(String)
    tab_url: Mapped[str | None] = mapped_column(String)
    notes: Mapped[str | None] = mapped_column(String)

    setlist_entries: Mapped[list["SetlistSong"]] = relationship(
        back_populates="song", cascade="all, delete-orphan"
    )
    footswitches: Mapped[list["SongFootswitch"]] = relationship(
        back_populates="song",
        cascade="all, delete-orphan",
        order_by="SongFootswitch.switch_slot",
    )
