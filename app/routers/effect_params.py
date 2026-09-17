from app.models.effect_params import EffectParams
from app.routers._crud import make_crud_router
from app.schemas.effect_params import EffectParamsCreate, EffectParamsRead, EffectParamsUpdate

router = make_crud_router(
    model=EffectParams,
    create_schema=EffectParamsCreate,
    update_schema=EffectParamsUpdate,
    read_schema=EffectParamsRead,
    prefix="/effect-params",
    tag="effect_params",
)
