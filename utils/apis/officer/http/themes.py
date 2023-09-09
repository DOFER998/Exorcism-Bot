from utils.apis.officer.http.client import officer_client


def get_themes():
    r = officer_client().get('/themes?language=all')
    return r.json()['data']


themes = get_themes()
