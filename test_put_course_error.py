import json


def test_index(app, client):
    data = {
    "description" : "This is brand new course",
    "title" : "Brand new course",
    "on_discount" : False,
    "price" : 25
    }

    response = client.put(
        "/course/1111",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 400
    
