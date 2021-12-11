import requests
import requests.exceptions
from django.conf import settings

def get_tax(price):
            tax = None
            try:
                #r = requests.get("http://localhost:8000/mwst/?cent={}".format(price), headers={"accept":"application/json"})
                r = requests.get("{}mwst/?cent={}".format(settings.TAX_CALC_API_URL,price),
                                 headers={"accept": "application/json"})
                print(r)
                if (r.status_code==200):
                    tax = r.json()["tax"]
            except requests.exceptions.ConnectionError:
                pass
            return tax