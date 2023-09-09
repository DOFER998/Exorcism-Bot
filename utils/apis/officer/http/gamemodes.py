from utils.apis.officer.http.client import officer_client


def get_gamemodes():
    r = officer_client().get('/gamemodes?language=all')
    return r.json()['data']


gamemodes = get_gamemodes()
