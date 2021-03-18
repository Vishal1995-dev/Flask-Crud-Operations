import json


def test_index(app, client):
    response = client.delete(
        "/course/1111",
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 404
