from pydantic import BaseModel, ConfigDict


class ReadSchema(BaseModel):
    """Base for response schemas: built from ORM objects, always carries id."""

    model_config = ConfigDict(from_attributes=True)

    id: str
