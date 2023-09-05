from utils.apis.officer.http.client import officer_client


def get_seasons():
    r = officer_client().get('/seasons?language=all')
    for season in r.json()['data']:
        seasons = {"_id": season['uuid']} | season
        return seasons


seasons = get_seasons()
