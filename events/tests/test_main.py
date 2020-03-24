import json

from fastapi.testclient import TestClient

from ..main import app
from ..models import Event


client = TestClient(app)

def test_list(db):
    response = client.get("/events/")

    assert response.status_code == 200
    assert response.json() == []

def test_create(db):
    client.post("/events/", json.dumps({"event": "TEST EVENT"}))

    event_count = db.query(Event).filter(
        Event.event.like("TEST EVENT")).count()

    assert event_count == 1
