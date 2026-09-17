from app.models.led_display import LedDisplay
from app.routers._crud import make_crud_router
from app.schemas.led_display import LedDisplayCreate, LedDisplayRead, LedDisplayUpdate

router = make_crud_router(
    model=LedDisplay,
    create_schema=LedDisplayCreate,
    update_schema=LedDisplayUpdate,
    read_schema=LedDisplayRead,
    prefix="/led-displays",
    tag="led_display",
)
