"""FastAPI application entrypoint."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import all_routers

app = FastAPI(
    title="ShedFX Backend",
    description="Control API for the ShedFX NAM floor unit. Runs on the Pi.",
    version="0.1.0",
)

# Origins the PWA may call this API from.
# TODO(Phase 2+): add the Pi's Tailscale hostname (e.g. http://<pi>.<tailnet>.ts.net)
# once it's known, so the installed PWA can reach the API remotely.
ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Vite dev server default
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in all_routers:
    app.include_router(router)


@app.get("/status", tags=["status"])
def get_status() -> dict:
    """Stub. Real Pi/JACK/NAM status check lands in Phase 2."""
    return {"current_effects_flow": None, "pi_status": "not_connected"}
