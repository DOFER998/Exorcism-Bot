from utils.apis.officer.http.client import officer_client


def get_themes():
    r = officer_client().get('/themes?language=all')
    for theme in r.json()['data']:
        themes = {"_id": theme['uuid']} | theme
        return themes


themes = get_themes()
