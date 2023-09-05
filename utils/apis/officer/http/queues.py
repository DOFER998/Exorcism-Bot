from utils.apis.officer.http.client import officer_client


def get_queues():
    r = officer_client().get('/gamemodes/queues?language=all')
    for queue in r.json()['data']:
        queues = {"_id": queue['uuid']} | queue
        return queues


queues = get_queues()
