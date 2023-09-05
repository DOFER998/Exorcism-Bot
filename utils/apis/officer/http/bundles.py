from utils.apis.officer.http.client import officer_client


def get_bundles():
    r = officer_client().get('/bundles?language=all')
    for bundle in r.json()['data']:
        bundles = {"_id": bundle['uuid']} | bundle
        return bundles


bundles = get_bundles()
