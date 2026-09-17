from app.models.song_footswitch import SongFootswitch
from app.routers._crud import make_crud_router
from app.schemas.song_footswitch import SongFootswitchCreate, SongFootswitchRead, SongFootswitchUpdate

router = make_crud_router(
    model=SongFootswitch,
    create_schema=SongFootswitchCreate,
    update_schema=SongFootswitchUpdate,
    read_schema=SongFootswitchRead,
    prefix="/song-footswitches",
    tag="song_footswitch",
)
