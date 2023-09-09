from utils.apis.officer.http.client import officer_client


def get_events():
    r = officer_client().get('/events?language=all')
    return r.json()['data']


events = get_events()
