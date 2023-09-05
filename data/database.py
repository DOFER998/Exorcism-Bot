import motor.motor_asyncio

from data.settings import settings

cluster = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
users = cluster.Exorcism_Bot.users
teams = cluster.Exorcism_Bot.teams
config = cluster.Exorcism_Bot.config
voice_channels = cluster.Exorcism_Bot.voice_channels


# add info
async def add_users(user_id):
    user = await users.find_one({"_id": str(user_id)})
    if not user:
        await users.insert_one(
            {
                "_id": str(user_id),
                "riot": None,
                "dis_id": str(user_id),
                "notify_mode": False,
                "notify": {},
                "DM_Message": True,
                "voice_start_time": None,
                "voice_time": None,
                "voice_settings": {
                    "name": None,
                    "limit": None,
                    "region": None,
                    "bitrate": None,
                    "lock": False,
                    "visible": False,
                    "chat": False,
                    "bans": [],
                    "trust": [],
                    "permissions": {},
                },
                "message_count": None,
                "reaction_count": None,
            }
        )
    else:
        pass
