import motor.motor_asyncio

from data.settings import settings
from utils.apis.officer.models import version

cluster = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
users = cluster.Exorcism_Bot.users
teams = cluster.Exorcism_Bot.teams
config = cluster.Exorcism_Bot.config
voice_channels = cluster.Exorcism_Bot.voice_channels
agents = cluster.Exorcism_Bot.agents
buddies = cluster.Exorcism_Bot.buddies
bundles = cluster.Exorcism_Bot.bundles
ceremonies = cluster.Exorcism_Bot.ceremonies
competitive_tiers = cluster.Exorcism_Bot.competitive_tiers
content_tiers = cluster.Exorcism_Bot.content_tiers
contracts = cluster.Exorcism_Bot.contracts
currencies = cluster.Exorcism_Bot.currencies
events = cluster.Exorcism_Bot.events
gamemodes = cluster.Exorcism_Bot.gamemodes
gear = cluster.Exorcism_Bot.gear
level_borders = cluster.Exorcism_Bot.level_borders
maps = cluster.Exorcism_Bot.maps
player_cards = cluster.Exorcism_Bot.player_cards
player_titles = cluster.Exorcism_Bot.player_titles
seasons = cluster.Exorcism_Bot.seasons
skins = cluster.Exorcism_Bot.skins
sprays = cluster.Exorcism_Bot.sprays
themes = cluster.Exorcism_Bot.themes
weapons = cluster.Exorcism_Bot.weapons
queues = cluster.Exorcism_Bot.queues


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


# add or update
async def add_version_in_db(data):
    await config.update_one({"_id": "val_version"}, {
        "$set": {"branch": data.branch, "buildDate": data.buildDate, "buildVersion": data.buildVersion,
                 "engineVersion": data.engineVersion, "manifestId": data.manifestId,
                 "riotClientBuild": data.riotClientBuild, "riotClientVersion": data.riotClientVersion,
                 "version": data.version}})


async def add_agents_in_db(data):
    agent = await agents.find_one({"_id": data["_id"]})
    if not agent:
        await agents.insert_one(data)
    else:
        pass


async def add_buddies_in_db(data):
    buddie = await buddies.find_one({"_id": data["_id"]})
    if not buddie:
        await buddies.insert_one(data)
    else:
        pass


async def add_bundles_in_db(data):
    bundle = await bundles.find_one({"_id": data["_id"]})
    if not bundle:
        await bundles.insert_one(data)
    else:
        pass


async def add_ceremonies_in_db(data):
    ceremonie = await ceremonies.find_one({"_id": data["_id"]})
    if not ceremonie:
        await ceremonies.insert_one(data)
    else:
        pass


async def add_competitive_tiers_in_db(data):
    competitive_tier = await competitive_tiers.find_one({"_id": data["_id"]})
    if not competitive_tier:
        await competitive_tiers.insert_one(data)
    else:
        pass


async def add_content_tiers_in_db(data):
    content_tier = await content_tiers.find_one({"_id": data["_id"]})
    if not content_tier:
        await content_tiers.insert_one(data)
    else:
        pass


async def add_contracts_in_db(data):
    contract = await contracts.find_one({"_id": data["_id"]})
    if not contract:
        await contracts.insert_one(data)
    else:
        pass


async def add_currencies_in_db(data):
    currencie = await currencies.find_one({"_id": data["_id"]})
    if not currencie:
        await currencies.insert_one(data)
    else:
        pass


async def add_events_in_db(data):
    event = await events.find_one({"_id": data["_id"]})
    if not event:
        await events.insert_one(data)
    else:
        pass


async def add_gamemodes_in_db(data):
    gamemode = await gamemodes.find_one({"_id": data["_id"]})
    if not gamemode:
        await gamemodes.insert_one(data)
    else:
        pass


async def add_gear_in_db(data):
    gea = await gear.find_one({"_id": data["_id"]})
    if not gea:
        await gear.insert_one(data)
    else:
        pass


async def add_level_borders_in_db(data):
    level_border = await level_borders.find_one({"_id": data["_id"]})
    if not level_border:
        await level_borders.insert_one(data)
    else:
        pass


async def add_maps_in_db(data):
    map = await maps.find_one({"_id": data["_id"]})
    if not map:
        await maps.insert_one(data)
    else:
        pass


async def add_player_cards_in_db(data):
    player_card = await player_cards.find_one({"_id": data["_id"]})
    if not player_card:
        await player_cards.insert_one(data)
    else:
        pass


async def add_player_titles_in_db(data):
    player_title = await player_titles.find_one({"_id": data["_id"]})
    if not player_title:
        await player_titles.insert_one(data)
    else:
        pass


async def add_seasons_in_db(data):
    season = await seasons.find_one({"_id": data["_id"]})
    if not season:
        await seasons.insert_one(data)
    else:
        pass


async def add_skins_in_db(data):
    skin = await skins.find_one({"_id": data["_id"]})
    if not skin:
        await skins.insert_one(data)
    else:
        pass


async def add_sprays_in_db(data):
    spray = await sprays.find_one({"_id": data["_id"]})
    if not spray:
        await sprays.insert_one(data)
    else:
        pass


async def add_themes_in_db(data):
    theme = await themes.find_one({"_id": data["_id"]})
    if not theme:
        await themes.insert_one(data)
    else:
        pass


async def add_weapons_in_db(data):
    weapon = await weapons.find_one({"_id": data["_id"]})
    if not weapon:
        await weapons.insert_one(data)
    else:
        pass


async def add_queues_in_db(data):
    queue = await queues.find_one({"_id": data["_id"]})
    if not queue:
        await queues.insert_one(data)
    else:
        pass


async def login_user_in_riot(user_id, data):
    await users.update_one({"_id": str(user_id)}, {"$set": {"riot": data}})


async def login_user_in_riot_update(user_id, cookie, access_token, expiry_token, entitlements_token):
    await users.update_one({"_id": str(user_id)}, {
        "$set": {"riot.cookie": cookie, "riot.access_token": access_token, "riot.expiry_token": expiry_token,
                 "riot.entitlements_token": entitlements_token}})


# get info
async def get_val_version() -> version.Version:
    val = await config.find_one({"_id": "val_version"})
    return version.Version.model_validate(val)


async def get_user(user_id):
    info = await users.find_one({"_id": str(user_id)})
    return info


async def get_skins_lvl_uuid(uuid):
    info = await skins.find_one({"levels.uuid": uuid})
    return info


async def get_content_tiers(uuid):
    info = await content_tiers.find_one({"_id": uuid})
    return info
