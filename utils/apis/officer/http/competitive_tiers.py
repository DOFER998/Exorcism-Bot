from utils.apis.officer.http.client import officer_client


def get_competitiveTiers():
    r = officer_client().get('/competitivetiers?language=all')
    return r.json()['data']


competitiveTiers = get_competitiveTiers()
