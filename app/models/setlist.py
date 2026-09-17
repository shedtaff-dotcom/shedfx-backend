from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models._mixins import UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.models.setlist_song import SetlistSong


class Setlist(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "setlist"

    name: Mapped[str] = mapped_column(String)
    gig_date: Mapped[str | None] = mapped_column(String)
    venue: Mapped[str | None] = mapped_column(String)
    notes: Mapped[str | None] = mapped_column(String)

    songs: Mapped[list["SetlistSong"]] = relationship(
        back_populates="setlist",
        cascade="all, delete-orphan",
        order_by="SetlistSong.position",
    )
