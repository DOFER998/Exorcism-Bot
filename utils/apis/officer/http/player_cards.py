from utils.apis.officer.http.client import officer_client


def get_player_cards():
    r = officer_client().get('/playercards?language=all')
    for player_card in r.json()['data']:
        player_cards = {"_id": player_card['uuid']} | player_card
        return player_cards


player_cards = get_player_cards()
