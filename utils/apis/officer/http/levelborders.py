from utils.apis.officer.http.client import officer_client


def get_levelBorders():
    r = officer_client().get('/levelborders?language=all')
    return r.json()['data']


levelBorders = get_levelBorders()
