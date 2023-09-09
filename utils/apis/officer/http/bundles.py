from utils.apis.officer.http.client import officer_client


def get_bundles():
    r = officer_client().get('/bundles?language=all')
    return r.json()['data']


bundles = get_bundles()
