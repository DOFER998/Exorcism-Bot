from utils.apis.officer.http.client import officer_client


def get_player_titles():
    r = officer_client().get('/playertitles?language=all')
    return r.json()['data']


player_titles = get_player_titles()
