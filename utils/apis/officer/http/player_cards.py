from utils.apis.officer.http.client import officer_client


def get_player_cards():
    r = officer_client().get('/playercards?language=all')
    return r.json()['data']


player_cards = get_player_cards()
