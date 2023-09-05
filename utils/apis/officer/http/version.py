from utils.apis.officer.http.client import officer_client
from utils.apis.officer.models.version import Version


def get_version() -> Version:
    r = officer_client().get('/version')
    pars = r.json()['data']
    return Version.model_validate(pars)


version = get_version()
