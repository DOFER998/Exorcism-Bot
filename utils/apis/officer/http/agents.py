from utils.apis.officer.http.client import officer_client


def get_agents():
    r = officer_client().get('/agents?isPlayableCharacter=true&language=all')
    for agent in r.json()['data']:
        agents = {"_id": agent['uuid']} | agent
        return agents


agents = get_agents()
