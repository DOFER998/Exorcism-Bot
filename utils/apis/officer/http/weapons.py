from utils.apis.officer.http.client import officer_client


def get_weapons():
    r = officer_client().get('/weapons?language=all')
    return r.json()['data']


weapons = get_weapons()
