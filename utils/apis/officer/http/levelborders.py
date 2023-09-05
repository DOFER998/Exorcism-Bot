from utils.apis.officer.http.client import officer_client


def get_levelBorders():
    r = officer_client().get('/levelborders?language=all')
    for levelBorder in r.json()['data']:
        levelBorders = {"_id": levelBorder['uuid']} | levelBorder
        return levelBorders


levelBorders = get_levelBorders()
