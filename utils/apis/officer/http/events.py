from utils.apis.officer.http.client import officer_client


def get_events():
    r = officer_client().get('/events?language=all')
    for event in r.json()['data']:
        events = {"_id": event['uuid']} | event
        return events


events = get_events()
