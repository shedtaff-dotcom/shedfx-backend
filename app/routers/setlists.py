from app.models.setlist import Setlist
from app.routers._crud import make_crud_router
from app.schemas.setlist import SetlistCreate, SetlistRead, SetlistUpdate

router = make_crud_router(
    model=Setlist,
    create_schema=SetlistCreate,
    update_schema=SetlistUpdate,
    read_schema=SetlistRead,
    prefix="/setlists",
    tag="setlist",
)
