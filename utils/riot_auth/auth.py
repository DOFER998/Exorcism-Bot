import json
import re
import ssl
from datetime import datetime, timedelta
from secrets import token_urlsafe
from typing import Any, Dict, Optional, Tuple

import aiohttp
import urllib3
from multidict import MultiDict

from utils.riot_auth.auth_exceptions import (
    RiotAuthenticationError,
    RiotAuthError,
    RiotMultifactorError,
    RiotRatelimitError,
    RiotUnknownErrorTypeError,
    RiotUnknownResponseTypeError,
)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def _extract_tokens(data: str) -> str:
    """Extract tokens from data"""

    pattern = re.compile('access_token=((?:[a-zA-Z]|\d|\.|-|_)*).*id_token=((?:[a-zA-Z]|\d|\.|-|_)*).*expires_in=(\d*)')
    response = pattern.findall(data['response']['parameters']['uri'])[0]
    return response


def _extract_tokens_from_uri(url: str) -> Optional[Tuple[str, Any]]:
    try:
        access_token = url.split("access_token=")[1].split("&scope")[0]
        token_id = url.split("id_token=")[1].split("&")[0]
        return access_token, token_id
    except IndexError as e:
        print(f"Cookies Invalid: {e}")


FORCED_CIPHERS = [
    'ECDHE-ECDSA-AES256-GCM-SHA384',
    'ECDHE-ECDSA-AES128-GCM-SHA256',
    'ECDHE-ECDSA-CHACHA20-POLY1305',
    'ECDHE-RSA-AES128-GCM-SHA256',
    'ECDHE-RSA-CHACHA20-POLY1305',
    'ECDHE-RSA-AES128-SHA256',
    'ECDHE-RSA-AES128-SHA',
    'ECDHE-RSA-AES256-SHA',
    'ECDHE-ECDSA-AES128-SHA256',
    'ECDHE-ECDSA-AES128-SHA',
    'ECDHE-ECDSA-AES256-SHA',
    'ECDHE+AES128',
    'ECDHE+AES256',
    'ECDHE+3DES',
    'RSA+AES128',
    'RSA+AES256',
    'RSA+3DES',
]


class ClientSession(aiohttp.ClientSession):
    def __init__(self, *args, **kwargs):
        ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        ctx.minimum_version = ssl.TLSVersion.TLSv1_3
        ctx.set_ciphers(':'.join(FORCED_CIPHERS))
        super().__init__(*args, **kwargs, cookie_jar=aiohttp.CookieJar(), connector=aiohttp.TCPConnector(ssl=ctx))


class Auth:
    RIOT_CLIENT_USER_AGENT = token_urlsafe(111)

    def __init__(self) -> None:
        self._headers: Dict = {
            'Content-Type': 'application/json',
            'User-Agent': Auth.RIOT_CLIENT_USER_AGENT,
            'Accept': 'application/json, text/plain, */*',
        }
        self.user_agent = Auth.RIOT_CLIENT_USER_AGENT

    async def authenticate(self, username: str, password: str) -> Optional[Dict[str, Any]]:
        """This function is used to authenticate the user."""

        session = ClientSession()

        data = {
            "client_id": "play-valorant-web-prod",
            "nonce": "1",
            "redirect_uri": "https://playvalorant.com/opt_in",
            "response_type": "token id_token",
            'scope': 'account openid',
        }

        r = await session.post('https://auth.riotgames.com/api/v1/authorization', json=data, headers=self._headers)

        cookies = {'cookie': {}}
        for cookie in r.cookies.items():
            cookies['cookie'][cookie[0]] = str(cookie).split('=')[1].split(';')[0]

        data = {"type": "auth", "username": username, "password": password, "remember": True}

        async with session.put('https://auth.riotgames.com/api/v1/authorization', json=data,
                               headers=self._headers) as r:
            data = await r.json()
            for cookie in r.cookies.items():
                cookies['cookie'][cookie[0]] = str(cookie).split('=')[1].split(';')[0]

        await session.close()

        if data['type'] == 'response':
            expiry_token = datetime.now() + timedelta(hours=1)

            response = _extract_tokens(data)
            access_token = response[0]
            token_id = response[1]

            expiry_token = datetime.now() + timedelta(minutes=59)
            cookies['expiry_token'] = int(datetime.timestamp(expiry_token))

            return {'auth': 'response', 'data': {'cookie': cookies, 'access_token': access_token, 'token_id': token_id}}

        elif data['type'] == 'multifactor':

            if r.status == 429:
                raise RiotRatelimitError('Пожалуйста, подождите несколько минут и повторите попытку')

            WaitFor2FA = {"auth": "2fa", "cookie": cookies, 'label': 'Вставьте 2FA код'}

            if data['multifactor']['method'] == 'email':
                WaitFor2FA[
                    'message'
                ] = f"Riot послал код на {data['multifactor']['email']}"
                return WaitFor2FA

            WaitFor2FA['message'] = 'У вас включена функция 2FA!'
            return WaitFor2FA

        raise RiotAuthenticationError(
            'Не удалось пройти аутентификацию. Убедитесь, что имя пользователя и пароль верны.')

    async def get_entitlements_token(self, access_token: str) -> Optional[str]:
        """This function is used to get the entitlements token."""

        session = ClientSession()

        headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}

        async with session.post('https://entitlements.auth.riotgames.com/api/token/v1', headers=headers, json={}) as r:
            data = await r.json()

        await session.close()
        try:
            entitlements_token = data['entitlements_token']
        except KeyError:
            raise RiotAuthenticationError('Срок действия cookie-файлов истек, выполните /login еще раз!')
        else:
            return entitlements_token

    async def get_userinfo(self, access_token: str) -> Tuple[str, str, str]:
        """This function is used to get the user info."""

        session = ClientSession()

        headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}

        async with session.post('https://auth.riotgames.com/userinfo', headers=headers, json={}) as r:
            data = await r.json()

        await session.close()
        try:
            puuid = data['sub']
            name = data['acct']['game_name']
            tag = data['acct']['tag_line']
        except KeyError:
            print('This user hasn\'t created a name or tagline yet.')
        else:
            return puuid, name, tag

    async def get_region(self, access_token: str, token_id: str) -> str:
        """This function is used to get the region."""

        session = ClientSession()

        headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}

        body = {"id_token": token_id}

        async with session.put(
                'https://riot-geo.pas.si.riotgames.com/pas/v1/product/valorant', headers=headers, json=body
        ) as r:
            data = await r.json()

        await session.close()
        try:
            region = data['affinities']['live']
        except KeyError:
            raise RiotUnknownErrorTypeError('Произошла неизвестная ошибка, пожалуйста, повторите `/login`')
        else:
            return region

    async def give2facode(self, code: str, cookies: Dict) -> Dict[str, Any]:
        """This function is used to give the 2FA code."""

        session = ClientSession()

        data = {"type": "multifactor", "code": code, "rememberDevice": True}

        async with session.put(
                'https://auth.riotgames.com/api/v1/authorization', headers=self._headers, json=data,
                cookies=cookies['cookie']
        ) as r:
            data = await r.json()

        await session.close()
        if data['type'] == 'response':
            cookies = {'cookie': {}}
            for cookie in r.cookies.items():
                cookies['cookie'][cookie[0]] = str(cookie).split('=')[1].split(';')[0]

            uri = data['response']['parameters']['uri']
            access_token, token_id = _extract_tokens_from_uri(uri)

            return {'auth': 'response', 'data': {'cookie': cookies, 'access_token': access_token, 'token_id': token_id}}

        raise RiotMultifactorError(
            'Не удалось выполнить многофакторную авторизацию. Убедитесь в правильности кода 2FA и повторите `/login`.')

    async def redeem_cookies(self, cookies: Dict) -> Tuple[Dict[str, Any], str, str]:
        """This function is used to redeem the cookies."""

        if isinstance(cookies, str):
            cookies = json.loads(cookies)

        session = ClientSession()

        if 'cookie' in cookies:
            cookies = cookies['cookie']

        async with session.get(
                "https://auth.riotgames.com/authorize?redirect_uri=https%3A%2F%2Fplayvalorant.com%2Fopt_in&client_id=play"
                "-valorant-web-prod&response_type=token%20id_token&scope=account%20openid&nonce=1",
                cookies=cookies,
                allow_redirects=False,
        ) as r:
            data = await r.text()

        if r.status != 303:
            raise RiotAuthenticationError('Срок действия cookie-файлов истек, пожалуйста, `/login` повторите!')

        if r.headers['Location'].startswith('/login'):
            raise RiotAuthenticationError('Срок действия cookie-файлов истек, пожалуйста, `/login` повторите!')

        old_cookie = cookies.copy()

        new_cookies = {'cookie': old_cookie}
        for cookie in r.cookies.items():
            new_cookies['cookie'][cookie[0]] = str(cookie).split('=')[1].split(';')[0]

        await session.close()

        accessToken, tokenId = _extract_tokens_from_uri(data)
        entitlements_token = await self.get_entitlements_token(accessToken)

        return new_cookies, accessToken, entitlements_token

    async def refresh_token(self, cookies: Dict) -> Tuple[Dict[str, Any], str, str]:
        return await self.redeem_cookies(cookies)
