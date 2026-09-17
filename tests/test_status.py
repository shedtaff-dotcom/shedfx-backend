def test_status_stub(client):
    resp = client.get("/status")
    assert resp.status_code == 200
    assert resp.json() == {"current_effects_flow": None, "pi_status": "not_connected"}
