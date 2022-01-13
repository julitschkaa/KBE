import requests
import requests.exceptions
from django.conf import settings


def get_gif_url(searchterm):
    """calls Giphys translate endpoint and returns an embeddable url to a gif specially chosen for your search term. c.f.https://developers.giphy.com/docs/api/endpoint/#translate """
    gif = None #find documetation for this object here https://developers.giphy.com/docs/api/schema#gif-object
    meta = None #find documentation for this object here https://developers.giphy.com/docs/api/schema#meta-object

    payload = {
        "api_key": settings.GIPHY_API_KEY,
        "s": searchterm,
        "weirdness": 10, #Value from 0-10 which makes results weirder as you go up the scale.
        "random_id": "e826c9fc5c929e0d6c6d423841a282aa" #An ID/proxy for a specific user.
    }
    try:
        print("{}gifs/translate".format(settings.GIPHY_API_URL))
        r = requests.get("{}gifs/translate".format(settings.GIPHY_API_URL),
                         params=payload,
                         headers={"accept": "application/json"})
        print(r)
        if (r.status_code==200):
            gif = r.json()["data"]
            meta = r.json()["meta"] #could probably be deleted
    except requests.exceptions.ConnectionError:
        return None
    return gif["embed_url"]