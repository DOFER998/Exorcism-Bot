from utils.apis.officer.http.client import officer_client


def get_seasons():
    r = officer_client().get('/seasons?language=all')
    return r.json()['data']


seasons = get_seasons()
