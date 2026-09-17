from app.models.effect import Effect
from app.routers._crud import make_crud_router
from app.schemas.effect import EffectCreate, EffectRead, EffectUpdate

router = make_crud_router(
    model=Effect,
    create_schema=EffectCreate,
    update_schema=EffectUpdate,
    read_schema=EffectRead,
    prefix="/effects",
    tag="effect",
)
