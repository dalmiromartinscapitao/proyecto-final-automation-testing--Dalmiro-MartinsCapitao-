import requests

def test_delete_user():
    r = requests.delete("https://jsonplaceholder.typicode.com/users/1")
    assert r.status_code == 200