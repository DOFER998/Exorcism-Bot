from utils.apis.officer.http.client import officer_client


def get_agents():
    r = officer_client().get('/agents?isPlayableCharacter=true&language=all')
    return r.json()['data']


agents = get_agents()
