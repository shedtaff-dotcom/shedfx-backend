"""FastAPI application entrypoint."""

from fastapi import FastAPI

from app.routers import all_routers

app = FastAPI(
    title="ShedFX Backend",
    description="Control API for the ShedFX NAM floor unit. Runs on the Pi.",
    version="0.1.0",
)

for router in all_routers:
    app.include_router(router)


@app.get("/status", tags=["status"])
def get_status() -> dict:
    """Stub. Real Pi/JACK/NAM status check lands in Phase 2."""
    return {"current_effects_flow": None, "pi_status": "not_connected"}
