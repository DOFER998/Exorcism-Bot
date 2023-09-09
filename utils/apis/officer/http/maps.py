from utils.apis.officer.http.client import officer_client


def get_maps():
    r = officer_client().get('/maps?language=all')
    return r.json()['data']


maps = get_maps()
