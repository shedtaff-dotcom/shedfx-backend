# docs/summary.md

# ShedFX

DIY guitar effects floor unit built around Neural Amp Modeler (NAM) and the
TONE3000 model library. A Raspberry Pi 5 runs real-time audio processing;
a cross-platform React PWA controls it from Android and iPad.

## What it does
Guitar → USB audio interface → Pi 5 → JACK + NAM LV2 engine → sound out.
A tablet or iPad running a web app switches presets, sees status, and
(eventually) drives physical footswitches and LED displays on a 3D-printed
floor enclosure. All audio stays on the Pi — the PWA is control-only, sending
HTTP commands and receiving JSON. Nothing audio-related ever touches the
tablet.

## Why
Replace the need for a commercial modelling unit (e.g. Line 6 Helix) for
home/studio use, using open tooling (NAM) and free community-captured amp
models (TONE3000).

## Repos
- `shedfx` — this repo. Docs, ERD, phase tracking.
- `shedfx-backend` — FastAPI (Python), runs on the Pi.
- `shedfx-frontend` — React PWA, single codebase for Android + iPad.

## Stack
| Layer | Technology |
|---|---|
| Pi OS | PatchboxOS |
| Audio engine | JACK + NAM LV2 plugin |
| Model library | TONE3000 / NAM captures |
| Backend | FastAPI (Python) + SQLite |
| Frontend | React PWA |
| Remote access | Tailscale |

## Data model
Core chain: `SETLIST → SETLIST_SONG → SONG → SONG_FOOTSWITCH (×4 slots) →
EFFECTS_FLOW → EFFECT (ordered chain) → EFFECT_MODEL → MODEL_LIBRARY`.
`EFFECTS_FLOW` also owns `LED_DISPLAY` and `FOOTSWITCH_MAP`. Full ERD in
`docs/data-model-v2.mermaid`.

## Status
Software foundation stage — repo scaffolding, backend CRUD, frontend
read-only views. No hardware connected yet. See `docs/phases.md`.

## Out of scope for now
- Variax integration
- Replacing the Helix Floor for live gigs
- Home studio DAW upgrade (separate project)