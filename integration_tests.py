import requests
import requests.exceptions

def test_calculate_tax_with_100_cents():
    tax = None
    r = requests.get("http://localhost/tax-calculator/?cent=100",headers={"accept": "application/json"})
    assert r.status_code == 200
    tax = r.json()["tax"]
    assert tax == 19

def test_check_size_of_API_produclist_is_10():
    r = requests.get("http://localhost/products/",headers={"accept": "application/json"})
    assert r.status_code == 200
    count = r.json()["count"]
    assert count == 10