from utils.apis.officer.http.client import officer_client


def get_sprays():
    r = officer_client().get('/sprays?language=all')
    for spray in r.json()['data']:
        sprays = {"_id": spray['uuid']} | spray
        return sprays


sprays = get_sprays()
