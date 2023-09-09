from utils.apis.officer.http import agents, buddies, bundles, ceremonies, competitive_tiers, content_tiers, contracts, \
    currencies, events, gamemodes, gear, levelborders, maps, player_cards, player_titles, queues, seasons, sprays, \
    themes, weapons, skins
from data.database import add_agents_in_db, add_buddies_in_db, add_bundles_in_db, add_ceremonies_in_db, \
    add_competitive_tiers_in_db, add_content_tiers_in_db, add_contracts_in_db, add_currencies_in_db, add_events_in_db, \
    add_gamemodes_in_db, add_gear_in_db, add_level_borders_in_db, add_maps_in_db, add_player_cards_in_db, \
    add_player_titles_in_db, add_queues_in_db, add_seasons_in_db, add_sprays_in_db, add_themes_in_db, add_weapons_in_db, \
    add_skins_in_db


async def agents_cache():
    for agent in agents.agents:
        a = {"_id": agent['uuid']} | agent
        await add_agents_in_db(data=a)


async def buddies_cache():
    for buddie in buddies.buddies:
        b = {"_id": buddie['uuid']} | buddie
        await add_buddies_in_db(data=b)


async def bundles_cache():
    for bundle in bundles.bundles:
        b = {"_id": bundle['uuid']} | bundle
        await add_bundles_in_db(data=b)


async def ceremonies_cache():
    for сeremonie in ceremonies.сeremonies:
        c = {"_id": сeremonie['uuid']} | сeremonie
        await add_ceremonies_in_db(data=c)


async def competitive_tiers_cache():
    for competitiveTier in competitive_tiers.competitiveTiers:
        c = {"_id": competitiveTier['uuid']} | competitiveTier
        await add_competitive_tiers_in_db(data=c)


async def content_tiers_cache():
    for сontentTier in content_tiers.сontentTiers:
        c = {"_id": сontentTier['uuid']} | сontentTier
        await add_content_tiers_in_db(data=c)


async def contracts_cache():
    for contract in contracts.contracts:
        c = {"_id": contract['uuid']} | contract
        await add_contracts_in_db(data=c)


async def currencies_cache():
    for currencie in currencies.currencies:
        c = {"_id": currencie['uuid']} | currencie
        await add_currencies_in_db(data=c)


async def events_cache():
    for event in events.events:
        e = {"_id": event['uuid']} | event
        await add_events_in_db(data=e)


async def gamemodes_cache():
    for gamemode in gamemodes.gamemodes:
        g = {"_id": gamemode['uuid']} | gamemode
        await add_gamemodes_in_db(data=g)


async def gear_cache():
    for gea in gear.gears:
        g = {"_id": gea['uuid']} | gea
        await add_gear_in_db(data=g)


async def levelborders_cache():
    for levelBorder in levelborders.levelBorders:
        l = {"_id": levelBorder['uuid']} | levelBorder
        await add_level_borders_in_db(data=l)


async def maps_cache():
    for map in maps.maps:
        m = {"_id": map['uuid']} | map
        await add_maps_in_db(data=m)


async def player_cards_cache():
    for player_card in player_cards.player_cards:
        p= {"_id": player_card['uuid']} | player_card
        await add_player_cards_in_db(data=p)


async def player_titles_cache():
    for player_title in player_titles.player_titles:
        p = {"_id": player_title['uuid']} | player_title
        await add_player_titles_in_db(data=p)


async def queues_cache():
    for queue in queues.queues:
        q = {"_id": queue['uuid']} | queue
        await add_queues_in_db(data=q)


async def seasons_cache():
    for season in seasons.seasons:
        s = {"_id": season['uuid']} | season
        await add_seasons_in_db(data=s)


async def sprays_cache():
    for spray in sprays.sprays:
        s = {"_id": spray['uuid']} | spray
        await add_sprays_in_db(data=s)


async def themes_cache():
    for theme in themes.themes:
        t = {"_id": theme['uuid']} | theme
        await add_themes_in_db(data=t)


async def weapons_cache():
    for weapon in weapons.weapons:
        w = {"_id": weapon['uuid']} | weapon
        await add_weapons_in_db(data=w)


async def skins_cache():
    for skin in skins.skins:
        s= {"_id": skin['uuid']} | skin
        await add_skins_in_db(data=s)


async def reload_cache():
    await agents_cache()
    await buddies_cache()
    await bundles_cache()
    await ceremonies_cache()
    await competitive_tiers_cache()
    await content_tiers_cache()
    await contracts_cache()
    await currencies_cache()
    await events_cache()
    await gamemodes_cache()
    await gear_cache()
    await levelborders_cache()
    await maps_cache()
    await player_cards_cache()
    await player_titles_cache()
    await queues_cache()
    await seasons_cache()
    await sprays_cache()
    await themes_cache()
    await weapons_cache()
    await skins_cache()
