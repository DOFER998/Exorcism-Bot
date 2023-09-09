from utils.apis.officer.http.client import officer_client


def get_currencies():
    r = officer_client().get('/currencies?language=all')
    return r.json()['data']


currencies = get_currencies()
