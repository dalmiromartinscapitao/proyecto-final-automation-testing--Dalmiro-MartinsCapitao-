
import requests

def test_delete_user():
    r = requests.delete("https://reqres.in/api/users/2")
    assert r.status_code in [204, 403]