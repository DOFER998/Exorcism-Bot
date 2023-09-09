from utils.apis.officer.http.client import officer_client


def get_contracts():
    r = officer_client().get('/contracts?language=all')
    return r.json()['data']


contracts = get_contracts()
