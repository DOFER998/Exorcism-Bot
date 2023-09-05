from utils.apis.officer.http.client import officer_client


def get_contracts():
    r = officer_client().get('/contracts?language=all')
    for contract in r.json()['data']:
        contracts = {"_id": contract['uuid']} | contract
        return contracts


contracts = get_contracts()
