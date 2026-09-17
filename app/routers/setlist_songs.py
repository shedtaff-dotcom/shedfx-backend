from app.models.setlist_song import SetlistSong
from app.routers._crud import make_crud_router
from app.schemas.setlist_song import SetlistSongCreate, SetlistSongRead, SetlistSongUpdate

router = make_crud_router(
    model=SetlistSong,
    create_schema=SetlistSongCreate,
    update_schema=SetlistSongUpdate,
    read_schema=SetlistSongRead,
    prefix="/setlist-songs",
    tag="setlist_song",
)
