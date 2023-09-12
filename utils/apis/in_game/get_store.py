from datetime import datetime, timedelta

from httpx import Client

from utils.time_utils import format_dt


def store_client(access_token, entitlements_token, region) -> Client:
    client = Client(
        headers={
            'Authorization': f'Bearer {access_token}',
            'X-Riot-Entitlements-JWT': f'{entitlements_token}',
        },
        base_url=f'https://pd.{region}.a.pvp.net'
    )
    return client


def get_store(access_token, entitlements_token, region, puuid) -> (list[str], str):
    try:
        r = store_client(access_token, entitlements_token, region).get(f'/store/v2/storefront/{puuid}')
        data = r.json()
        skin_panel = data['SkinsPanelLayout']
        pulling = []
        for i in skin_panel['SingleItemStoreOffers']:
            pulling.append(i)
        skins = []
        for r in pulling:
            skins.append({'id': r['OfferID'].lower(), 'cost': r['Cost']['85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741']})
        return skins, format_dt(
            datetime.utcnow() + timedelta(seconds=skin_panel['SingleItemOffersRemainingDurationInSeconds']))
    except KeyError:
        return None


def get_accessory_store(access_token, entitlements_token, region, puuid) -> (list[str], str):
    r = store_client(access_token, entitlements_token, region).get(f'/store/v2/storefront/{puuid}')
    data = r.json()
    panel = data['AccessoryStore']
    pulling = []
    for i in panel['AccessoryStoreOffers']:
        pulling.append(i)
    item = []
    for u in pulling:
        item.append(u)
    return item, format_dt(
        datetime.utcnow() + timedelta(seconds=panel['AccessoryStoreRemainingDurationInSeconds']))
