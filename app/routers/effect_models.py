from app.models.effect_model import EffectModel
from app.routers._crud import make_crud_router
from app.schemas.effect_model import EffectModelCreate, EffectModelRead, EffectModelUpdate

router = make_crud_router(
    model=EffectModel,
    create_schema=EffectModelCreate,
    update_schema=EffectModelUpdate,
    read_schema=EffectModelRead,
    prefix="/effect-models",
    tag="effect_model",
)
