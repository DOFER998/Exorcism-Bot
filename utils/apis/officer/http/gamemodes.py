from utils.apis.officer.http.client import officer_client


def get_gamemodes():
    r = officer_client().get('/gamemodes?language=all')
    for gamemode in r.json()['data']:
        gamemodes = {"_id": gamemode['uuid']} | gamemode
        return gamemodes


gamemodes = get_gamemodes()
