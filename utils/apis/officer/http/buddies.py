from utils.apis.officer.http.client import officer_client


def get_buddies():
    r = officer_client().get('/buddies?language=all')
    return r.json()['data']


buddies = get_buddies()
