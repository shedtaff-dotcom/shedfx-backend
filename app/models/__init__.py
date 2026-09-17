"""SQLAlchemy models, one file per ERD entity. Importing this package
registers every table on ``Base.metadata`` for Alembic and tests."""

from app.database import Base
from app.models.effect import Effect
from app.models.effect_model import EffectModel
from app.models.effect_params import EffectParams
from app.models.effects_flow import EffectsFlow
from app.models.footswitch_map import FootswitchMap
from app.models.led_display import LedDisplay
from app.models.model_library import ModelLibrary
from app.models.setlist import Setlist
from app.models.setlist_song import SetlistSong
from app.models.song import Song
from app.models.song_footswitch import SongFootswitch

__all__ = [
    "Base",
    "Effect",
    "EffectModel",
    "EffectParams",
    "EffectsFlow",
    "FootswitchMap",
    "LedDisplay",
    "ModelLibrary",
    "Setlist",
    "SetlistSong",
    "Song",
    "SongFootswitch",
]
