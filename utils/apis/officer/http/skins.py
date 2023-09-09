from utils.apis.officer.http.client import officer_client


def get_skins():
    r = officer_client().get('/weapons/skins?language=all')
    return r.json()['data']


skins = get_skins()
