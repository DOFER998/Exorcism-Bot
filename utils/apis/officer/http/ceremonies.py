from utils.apis.officer.http.client import officer_client


def get_сeremonies():
    r = officer_client().get('/ceremonies?language=all')
    for сeremonie in r.json()['data']:
        сeremonies = {"_id": сeremonie['uuid']} | сeremonie
        return сeremonies


сeremonies = get_сeremonies()
