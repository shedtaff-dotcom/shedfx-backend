"""FastAPI routers, one per entity. ``all_routers`` is mounted by main.py."""

from app.routers import (
    effect_models,
    effect_params,
    effects,
    effects_flows,
    footswitch_maps,
    led_displays,
    model_libraries,
    setlist_songs,
    setlists,
    song_footswitches,
    songs,
)

all_routers = [
    setlists.router,
    setlist_songs.router,
    songs.router,
    song_footswitches.router,
    effects_flows.router,
    led_displays.router,
    footswitch_maps.router,
    effects.router,
    effect_params.router,
    effect_models.router,
    model_libraries.router,
]
