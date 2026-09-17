from app.models.footswitch_map import FootswitchMap
from app.routers._crud import make_crud_router
from app.schemas.footswitch_map import FootswitchMapCreate, FootswitchMapRead, FootswitchMapUpdate

router = make_crud_router(
    model=FootswitchMap,
    create_schema=FootswitchMapCreate,
    update_schema=FootswitchMapUpdate,
    read_schema=FootswitchMapRead,
    prefix="/footswitch-maps",
    tag="footswitch_map",
)
