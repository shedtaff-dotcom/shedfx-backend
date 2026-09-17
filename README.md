# shedfx-backend

FastAPI control API for [ShedFX](https://github.com/shedtaff-dotcom/shedfx),
a DIY guitar effects floor unit built on a Raspberry Pi 5 running
[Neural Amp Modeler](https://www.neuralampmodeler.com/) via JACK. This
service runs on the Pi and is driven over HTTP by the
[shedfx-frontend](https://github.com/shedtaff-dotcom/shedfx-frontend) React PWA.

**Status:** software foundation. CRUD scaffolding plus a stubbed `/status`
endpoint. No audio, GPIO, or LED code yet — see the
[phase tracker](https://github.com/shedtaff-dotcom/shedfx/blob/main/docs/phases.md).

## Layout

```
app/
  main.py        FastAPI entrypoint, mounts routers, /status stub
  database.py    SQLite engine, session factory, declarative Base
  models/        SQLAlchemy models — one file per entity
  schemas/       Pydantic request/response schemas
  routers/       one CRUD router per entity
alembic/         migrations (SQLite, batch mode)
tests/           pytest suite, in-memory SQLite
```

## Run locally

```bash
python -m venv .venv
.venv/Scripts/activate        # Windows; use source .venv/bin/activate on the Pi
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```

Interactive docs at http://127.0.0.1:8000/docs.

## Tests

```bash
pytest
```

## Migrations

Models are the source of truth. After changing one:

```bash
alembic revision --autogenerate -m "describe change"
alembic upgrade head
```

## Configuration

See `.env.example`. `TONE3000_API_KEY` and `TAILSCALE_HOSTNAME` are
reserved and unused for now.

**Tailscale note:** remote access to the Pi is handled by Tailscale at the
OS level, not by this app. The app binds to whatever interface uvicorn is
given; the PWA reaches it via the Pi's Tailscale hostname.

## Related repos

- [shedfx](https://github.com/shedtaff-dotcom/shedfx) — docs, ERD, phase tracking
- [shedfx-frontend](https://github.com/shedtaff-dotcom/shedfx-frontend) — React PWA

## License

MIT — see [LICENSE](LICENSE).
