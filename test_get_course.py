import json


def test_index(app, client):
    res = client.get('/course/1')
    assert res.status_code == 200
    expected = {
    "data": {
        "id": 1,
        "date_created": "2019-12-25 12:57:58",
        "date_updated": "2020-12-18 16:18:29",
        "description": "Scala is a multi-paradigm, general-purpose programming language.",
        "discount_price": 2,
        "image_path": "",
        "on_discount": False,
        "price": 20,
        "title": "The Art of Scala"
    }
}
    assert expected == json.loads(res.get_data(as_text=True))
