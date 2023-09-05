from utils.apis.officer.http.client import officer_client


def get_gears():
    r = officer_client().get('/gear?language=all')
    for gear in r.json()['data']:
        gears = {"_id": gear['uuid']} | gear
        return gears


gears = get_gears()
