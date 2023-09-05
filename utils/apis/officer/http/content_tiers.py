from utils.apis.officer.http.client import officer_client


def get_сontentTiers():
    r = officer_client().get('/contenttiers?language=all')
    for сontentTier in r.json()['data']:
        сontentTiers = {"_id": сontentTier['uuid']} | сontentTier
        return сontentTiers


сontentTiers = get_сontentTiers()
