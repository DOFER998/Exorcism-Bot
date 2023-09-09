from utils.apis.officer.http.client import officer_client


def get_сontentTiers():
    r = officer_client().get('/contenttiers?language=all')
    return r.json()['data']


сontentTiers = get_сontentTiers()
