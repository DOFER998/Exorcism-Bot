from utils.apis.officer.http.client import officer_client


def get_sprays():
    r = officer_client().get('/sprays?language=all')
    return r.json()['data']


sprays = get_sprays()
