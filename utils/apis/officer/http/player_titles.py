from utils.apis.officer.http.client import officer_client


def get_player_titles():
    r = officer_client().get('/playertitles?language=all')
    for player_title in r.json()['data']:
        player_titles = {"_id": player_title['uuid']} | player_title
        return player_titles


player_titles = get_player_titles()
