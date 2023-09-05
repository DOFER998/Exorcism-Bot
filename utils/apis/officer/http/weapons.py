from utils.apis.officer.http.client import officer_client


def get_weapons():
    r = officer_client().get('/weapons?language=all')
    for weapon in r.json()['data']:
        weapons = {"_id": weapon['uuid']} | weapon
        return weapons


weapons = get_weapons()
