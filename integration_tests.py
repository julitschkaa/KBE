import os

import requests
import requests.exceptions
from pymongo import MongoClient


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

def test_compare_size_of_API_produclist_with_mangodb2():
    r = requests.get("http://localhost/products/",headers={"accept": "application/json"})
    assert r.status_code == 200
    count = r.json()["count"]
    # open connection to mangodb2
    client = MongoClient("localhost", port=8081, username=os.environ.get("MANGODB2_USERNAME"),
                         password=os.environ.get("MANGODB2_PASSWORD"), authMechanism='SCRAM-SHA-256')
    db = client["mangodb2"]
    # check if a collection named products already exists
    collectionnames = db.list_collection_names()
    assert "products" in collectionnames
    mangocount = db.products.count_documents({})
    assert count == mangocount