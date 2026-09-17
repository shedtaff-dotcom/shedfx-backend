from app.models.song import Song
from app.routers._crud import make_crud_router
from app.schemas.song import SongCreate, SongRead, SongUpdate

router = make_crud_router(
    model=Song,
    create_schema=SongCreate,
    update_schema=SongUpdate,
    read_schema=SongRead,
    prefix="/songs",
    tag="song",
)
