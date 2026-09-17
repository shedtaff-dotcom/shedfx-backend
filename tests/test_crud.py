"""One create-then-fetch test per entity, via the HTTP API.

Deliberately shallow: proves each model round-trips through its router.
Deeper behavioural tests come with the real API design."""


def _create(client, path: str, payload: dict) -> dict:
    resp = client.post(path, json=payload)
    assert resp.status_code == 201, resp.text
    return resp.json()


def _fetch(client, path: str, item_id: str) -> dict:
    resp = client.get(f"{path}/{item_id}")
    assert resp.status_code == 200, resp.text
    return resp.json()


# --- builders for parent rows ---------------------------------------------


def _setlist(client) -> dict:
    return _create(client, "/setlists", {"name": "Friday gig", "venue": "The Shed"})


def _song(client) -> dict:
    return _create(client, "/songs", {"title": "Comfortably Numb", "artist": "Pink Floyd", "bpm": 63})


def _effects_flow(client) -> dict:
    return _create(client, "/effects-flows", {"name": "Clean", "input_gain": 0.0, "output_gain": 0.0})


def _model_library(client) -> dict:
    return _create(client, "/model-libraries", {"source": "tone3000", "category": "amp"})


def _effect_model(client) -> dict:
    lib = _model_library(client)
    return _create(
        client,
        "/effect-models",
        {"model_library_id": lib["id"], "name": "JCM800", "type": "nam", "file_path": "/models/jcm800.nam"},
    )


def _effect(client) -> dict:
    flow = _effects_flow(client)
    model = _effect_model(client)
    return _create(
        client,
        "/effects",
        {"effects_flow_id": flow["id"], "effect_model_id": model["id"], "chain_position": 1},
    )


# --- one test per entity ----------------------------------------------------


def test_setlist(client):
    created = _setlist(client)
    assert _fetch(client, "/setlists", created["id"])["name"] == "Friday gig"


def test_song(client):
    created = _song(client)
    assert _fetch(client, "/songs", created["id"])["title"] == "Comfortably Numb"


def test_setlist_song(client):
    setlist, song = _setlist(client), _song(client)
    created = _create(
        client, "/setlist-songs", {"setlist_id": setlist["id"], "song_id": song["id"], "position": 1}
    )
    fetched = _fetch(client, "/setlist-songs", created["id"])
    assert fetched["setlist_id"] == setlist["id"] and fetched["position"] == 1


def test_effects_flow(client):
    created = _effects_flow(client)
    assert _fetch(client, "/effects-flows", created["id"])["name"] == "Clean"


def test_song_footswitch(client):
    song, flow = _song(client), _effects_flow(client)
    created = _create(
        client,
        "/song-footswitches",
        {"song_id": song["id"], "effects_flow_id": flow["id"], "switch_slot": 2},
    )
    assert _fetch(client, "/song-footswitches", created["id"])["switch_slot"] == 2


def test_led_display(client):
    flow = _effects_flow(client)
    created = _create(
        client,
        "/led-displays",
        {"effects_flow_id": flow["id"], "label": "CLN", "colour": "#00ff00", "brightness": 80},
    )
    assert _fetch(client, "/led-displays", created["id"])["label"] == "CLN"


def test_model_library(client):
    created = _model_library(client)
    assert _fetch(client, "/model-libraries", created["id"])["source"] == "tone3000"


def test_effect_model(client):
    created = _effect_model(client)
    assert _fetch(client, "/effect-models", created["id"])["name"] == "JCM800"


def test_effect(client):
    created = _effect(client)
    fetched = _fetch(client, "/effects", created["id"])
    assert fetched["chain_position"] == 1 and fetched["enabled"] is True


def test_effect_params(client):
    effect = _effect(client)
    created = _create(
        client,
        "/effect-params",
        {"effect_id": effect["id"], "param_name": "gain", "value": 0.5, "min": 0.0, "max": 1.0},
    )
    assert _fetch(client, "/effect-params", created["id"])["param_name"] == "gain"


def test_footswitch_map(client):
    effect = _effect(client)
    created = _create(
        client,
        "/footswitch-maps",
        {
            "effects_flow_id": effect["effects_flow_id"],
            "switch_number": 1,
            "action": "toggle",
            "target_effect_id": effect["id"],
        },
    )
    assert _fetch(client, "/footswitch-maps", created["id"])["action"] == "toggle"


# --- a couple of cheap guard-rails -----------------------------------------


def test_get_missing_returns_404(client):
    assert client.get("/songs/nope").status_code == 404


def test_bad_foreign_key_returns_409(client):
    resp = client.post(
        "/effect-models", json={"model_library_id": "nope", "name": "x"}
    )
    assert resp.status_code == 409


def test_update_and_delete(client):
    song = _song(client)
    resp = client.put(f"/songs/{song['id']}", json={"bpm": 120})
    assert resp.status_code == 200 and resp.json()["bpm"] == 120
    assert client.delete(f"/songs/{song['id']}").status_code == 204
    assert client.get(f"/songs/{song['id']}").status_code == 404
