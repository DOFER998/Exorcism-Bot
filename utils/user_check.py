import time
import asyncio
from data.database import get_user, login_user_in_riot_update
from datetime import datetime, timedelta
from utils.riot_auth.auth import Auth


async def check_user(user_id):
    user = await get_user(user_id)
    auth = Auth()
    try:
        if time.time() > user['riot']['expiry_token']:
            cookies, access_token, entitlements_token = await auth.redeem_cookies(user['riot']['cookie'])
            expired_cookie = datetime.timestamp(datetime.utcnow() + timedelta(minutes=59))
            await login_user_in_riot_update(user_id=user_id, cookie=cookies, access_token=access_token,
                                            expiry_token=expired_cookie, entitlements_token=entitlements_token)
            return user
        else:
            return user
    except TypeError:
        return None
