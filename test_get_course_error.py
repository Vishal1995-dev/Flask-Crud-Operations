import json


def test_index(app, client):
    res = client.get('/course/1111')
    assert res.status_code == 404
    
