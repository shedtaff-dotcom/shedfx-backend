from app.models.model_library import ModelLibrary
from app.routers._crud import make_crud_router
from app.schemas.model_library import ModelLibraryCreate, ModelLibraryRead, ModelLibraryUpdate

router = make_crud_router(
    model=ModelLibrary,
    create_schema=ModelLibraryCreate,
    update_schema=ModelLibraryUpdate,
    read_schema=ModelLibraryRead,
    prefix="/model-libraries",
    tag="model_library",
)
