from utils.apis.officer.http.client import officer_client


def get_currencies():
    r = officer_client().get('/currencies?language=all')
    for currencie in r.json()['data']:
        currencies = {"_id": currencie['uuid']} | currencie
        return currencies


currencies = get_currencies()
