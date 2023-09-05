from utils.apis.officer.http.client import officer_client


def get_competitiveTiers():
    r = officer_client().get('/competitivetiers?language=all')
    for competitiveTier in r.json()['data']:
        competitiveTiers = {"_id": competitiveTier['uuid']} | competitiveTier
        return competitiveTiers


competitiveTiers = get_competitiveTiers()
