import requests
import requests.exceptions

def get_tax(price):
            tax = None
            try:
                r = requests.get("http://localhost:8000/mwst/?cent={}".format(price), headers={"accept":"application/json"})
                if (r.status_code==200):
                    tax = r.json()["tax"]
            except requests.exceptions.ConnectionError:
                pass
            return tax