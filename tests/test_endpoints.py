import pytest
import requests

url = 'http://127.0.0.1:5000'

def test_index_page():
    r = requests.get(url+'/greet')
    assert r.status_code == 200