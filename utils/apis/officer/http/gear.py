from utils.apis.officer.http.client import officer_client


def get_gears():
    r = officer_client().get('/gear?language=all')
    return r.json()['data']


gears = get_gears()
