import httpx
from datetime import datetime, timedelta

from utils.time_utils import format_dt


class GetStore(httpx.AsyncClient):
    def __init__(self, access_token, entitlements_token, region, puuid):
        self.access_token = access_token
        self.entitlements_token = entitlements_token
        self.region = region
        self.puuid = puuid
        super().__init__(
            headers={
                'Authorization': f'Bearer {self.access_token}',
                'X-Riot-Entitlements-JWT': f'{self.entitlements_token}',
                "X-Riot-ClientPlatform": "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9",
                "X-Riot-ClientVersion": "release-07.01-shipping-28-925799"
            },
            base_url=f'https://pd.{self.region}.a.pvp.net'
        )

    async def get_daily_store(self) -> (list[str], str):
        try:
            session = GetStore(self.access_token, self.entitlements_token, self.region, self.puuid)
            r = await session.get(f'/store/v2/storefront/{self.puuid}')
            data = r.json()
            skin_panel = data['SkinsPanelLayout']
            pulling = []
            for i in skin_panel['SingleItemStoreOffers']:
                pulling.append(i)
            skins = []
            for r in pulling:
                skins.append({'id': r['OfferID'].lower(), 'cost': r['Cost']['85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741']})
            await session.aclose()
            return skins, format_dt(
                datetime.utcnow() + timedelta(seconds=skin_panel['SingleItemOffersRemainingDurationInSeconds']))
        except KeyError:
            return None

    async def get_accessory_store(self) -> (list[str], str):
        session = GetStore(self.access_token, self.entitlements_token, self.region, self.puuid)
        r = await session.get(f'/store/v2/storefront/{self.puuid}')
        data = r.json()
        panel = data['AccessoryStore']
        pulling = []
        for i in panel['AccessoryStoreOffers']:
            pulling.append(i)
        item = []
        for u in pulling:
            item.append(u)
        await session.aclose()
        return item, format_dt(
            datetime.utcnow() + timedelta(seconds=panel['AccessoryStoreRemainingDurationInSeconds']))

    async def get_night_market(self) -> (list[str], str):
        try:
            session = GetStore(self.access_token, self.entitlements_token, self.region, self.puuid)
            r = await session.get(f'/store/v2/storefront/{self.puuid}')
            data = r.json()
            night_market = data["BonusStore"]
            night_market_offers = night_market["BonusStoreOffers"]
            skins = []
            for item in night_market_offers:
                uuid: str = item["Offer"]["OfferID"].lower()
                og_cost: int = item["Offer"]["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]
                discounted_p: int = item["DiscountPercent"]
                discounted_cost: int = item["DiscountCosts"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]
                skins.append(
                    {'id': uuid, 'og_cost': og_cost, 'discounted_p': discounted_p, 'discounted_cost': discounted_cost})
            return skins, format_dt(
                datetime.utcnow() + timedelta(seconds=night_market["BonusStoreRemainingDurationInSeconds"]))
        except KeyError:
            return None
