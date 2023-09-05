from utils.apis.officer.http.client import officer_client


def get_buddies():
    r = officer_client().get('/buddies?language=all')
    for buddie in r.json()['data']:
        buddies = {"_id": buddie['uuid']} | buddie
        return buddies


buddies = get_buddies()
