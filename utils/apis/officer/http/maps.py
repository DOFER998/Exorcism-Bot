from utils.apis.officer.http.client import officer_client


def get_maps():
    r = officer_client().get('/maps?language=all')
    for map in r.json()['data']:
        maps = {"_id": map['uuid']} | map
        return maps


maps = get_maps()
