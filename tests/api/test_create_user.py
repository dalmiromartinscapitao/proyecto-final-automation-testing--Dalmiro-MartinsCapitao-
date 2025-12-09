import requests

def test_create_user():
    payload = {"name": "Juan", "job": "QA"}
    r = requests.post("https://jsonplaceholder.typicode.com/users", json=payload)
    assert r.status_code == 201 or r.status_code == 200