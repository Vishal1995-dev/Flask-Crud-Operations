import json


def test_index(app, client):
    response = client.delete(
        "/course/110",
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
    assert response.data == b"Specified course deleted"
