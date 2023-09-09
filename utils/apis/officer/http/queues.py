from utils.apis.officer.http.client import officer_client


def get_queues():
    r = officer_client().get('/gamemodes/queues?language=all')
    return r.json()['data']


queues = get_queues()
