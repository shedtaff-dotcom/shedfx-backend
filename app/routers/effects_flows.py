from app.models.effects_flow import EffectsFlow
from app.routers._crud import make_crud_router
from app.schemas.effects_flow import EffectsFlowCreate, EffectsFlowRead, EffectsFlowUpdate

router = make_crud_router(
    model=EffectsFlow,
    create_schema=EffectsFlowCreate,
    update_schema=EffectsFlowUpdate,
    read_schema=EffectsFlowRead,
    prefix="/effects-flows",
    tag="effects_flow",
)
