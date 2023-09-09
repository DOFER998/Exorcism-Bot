from utils.apis.officer.http.client import officer_client


def get_сeremonies():
    r = officer_client().get('/ceremonies?language=all')
    return r.json()['data']


сeremonies = get_сeremonies()
