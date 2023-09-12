import discord

from data.database import get_sprays, get_buddies_lvl_uuid, get_player_cards, get_player_titles, get_skins_lvl_uuid, \
    get_content_tiers
from data.settings import png, tiers_color, color, emoji
from utils.apis.in_game.get_store import get_store, get_accessory_store
from utils.user_check import check_user


class SwitchingBetweenStores(discord.ui.View):
    def __init__(self, interaction: discord.Interaction):
        super().__init__(timeout=30, disable_on_timeout=True)
        self.interaction = interaction

    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True
        await self.interaction.edit_original_response(view=self)

    @discord.ui.button(style=discord.ButtonStyle.green,
                       emoji=discord.PartialEmoji.from_str(emoji.expand), custom_id="expand_store")
    async def image(self, button: discord.ui.Button, interaction: discord.Interaction):
        new_embeds = []
        for embed in interaction.message.embeds:
            if (type(embed.image.url) == str and "nm" in embed.image.url.lower()) or (
                    type(embed.thumbnail.url) == str and "nm" in embed.thumbnail.url.lower()):
                new_embeds.append(embed)
                continue
            if 'expand' in button.emoji.name:
                new_emoji = discord.PartialEmoji.from_str(emoji.shrink)
                if embed.thumbnail:
                    embed.set_image(url=embed.thumbnail.url)
                    embed.set_thumbnail(url=discord.Embed.Empty)
            elif 'shrink' in button.emoji.name:
                new_emoji = discord.PartialEmoji.from_str(emoji.expand)
                if embed.image:
                    embed.set_thumbnail(url=embed.image.url)
                    embed.set_image(url=png.line)
            new_embeds.append(embed)
        button.emoji = new_emoji
        await interaction.response.edit_message(embeds=new_embeds, view=self)

    @discord.ui.button(style=discord.ButtonStyle.blurple, label='Магазин аксессуаров', custom_id='daily_shop')
    async def shop(self, button: discord.ui.Button, interaction: discord.Interaction):
        user_riot_info = await check_user(user_id=str(interaction.message.interaction.user.id))
        store_info = get_store(
            access_token=user_riot_info['riot']['access_token'],
            entitlements_token=user_riot_info['riot']['entitlements_token'],
            region=user_riot_info['riot']['region'],
            puuid=user_riot_info['riot']['puuid']
        )
        accessory_store_info = get_accessory_store(
            access_token=user_riot_info['riot']['access_token'],
            entitlements_token=user_riot_info['riot']['entitlements_token'],
            region=user_riot_info['riot']['region'],
            puuid=user_riot_info['riot']['puuid']
        )
        new_embeds = []
        if 'Магазин аксессуаров' in button.label:
            new_label = 'Ежедневный магазин'
            self.image.disabled = True
            embed = discord.Embed(title=" ",
                                  description=f"Магазин аксессуаров `{user_riot_info['riot']['player_name']}`\nОсталось времени до смены: {accessory_store_info[1]}",
                                  color=color.main_color)
            embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon.url)
            embed.set_image(url=png.line)
            new_embeds.append(embed)
            for item in accessory_store_info[0]:
                if item['Offer']['Rewards'][0]['ItemTypeID'] == 'd5f120f8-ff8c-4aac-92ea-f2b5acbe9475':  # Sprays
                    sprays = await get_sprays(uuid=item['Offer']['Rewards'][0]['ItemID'])
                    sprays_embed = discord.Embed(title=sprays['displayName']['ru-RU'],
                                                 description=f"{emoji.k_credit} `{item['Offer']['Cost']['85ca954a-41f2-ce94-9b45-8ca3dd39a00d']}`",
                                                 color=color.main_color)
                    sprays_embed.set_thumbnail(url=sprays['fullTransparentIcon'] or sprays['displayIcon'])
                    sprays_embed.set_image(url=png.line)
                    new_embeds.append(sprays_embed)
                if item['Offer']['Rewards'][0]['ItemTypeID'] == 'dd3bf334-87f3-40bd-b043-682a57a8dc3a':  # Gun Buddies
                    gun_buddies = await get_buddies_lvl_uuid(uuid=[item['Offer']['Rewards'][0]['ItemID']])
                    gun_buddies_embed = discord.Embed(title=gun_buddies['displayName']['ru-RU'],
                                                      description=f"{emoji.k_credit} `{item['Offer']['Cost']['85ca954a-41f2-ce94-9b45-8ca3dd39a00d']}`",
                                                      color=color.main_color)
                    gun_buddies_embed.set_thumbnail(url=gun_buddies['displayIcon'])
                    gun_buddies_embed.set_image(url=png.line)
                    new_embeds.append(gun_buddies_embed)
                if item['Offer']['Rewards'][0]['ItemTypeID'] == '3f296c07-64c3-494c-923b-fe692a4fa1bd':  # Player Cards
                    player_cards = await get_player_cards(uuid=item['Offer']['Rewards'][0]['ItemID'])
                    player_cards_embed = discord.Embed(title=player_cards['displayName']['ru-RU'],
                                                       description=f"{emoji.k_credit} `{item['Offer']['Cost']['85ca954a-41f2-ce94-9b45-8ca3dd39a00d']}`",
                                                       color=color.main_color)
                    player_cards_embed.set_thumbnail(url=player_cards['largeArt'])
                    player_cards_embed.set_image(url=player_cards['wideArt'])
                    new_embeds.append(player_cards_embed)
                if item['Offer']['Rewards'][0]['ItemTypeID'] == 'de7caa6b-adf7-4588-bbd1-143831e786c6':  # Player titles
                    player_titles = await get_player_titles(uuid=item['Offer']['Rewards'][0]['ItemID'])
                    player_titles_embed = discord.Embed(title=player_titles['displayName']['ru-RU'],
                                                        description=f"{emoji.k_credit} `{item['Offer']['Cost']['85ca954a-41f2-ce94-9b45-8ca3dd39a00d']}`",
                                                        color=color.main_color)
                    player_titles_embed.set_thumbnail(url=png.titles)
                    player_titles_embed.set_image(url=png.line)
                    new_embeds.append(player_titles_embed)
        elif 'Ежедневный магазин' in button.label:
            new_label = 'Магазин аксессуаров'
            self.image.disabled = False
            embed = discord.Embed(title=" ",
                                  description=f"Ежедневный магазин `{user_riot_info['riot']['player_name']}`\nОсталось времени до смены: {store_info[1]}",
                                  color=color.main_color)
            embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon.url)
            embed.set_image(url=png.line)
            new_embeds.append(embed)
            for skin in store_info[0]:
                skin_info = await get_skins_lvl_uuid(skin['id'])
                tiers = await get_content_tiers(skin_info['contentTierUuid'])
                skin_embed = discord.Embed(title=" ",
                                           description=f"{emoji.v_point} `{skin['cost']}`",
                                           color=tiers_color[skin_info['contentTierUuid']])
                skin_embed.set_author(name=skin_info['displayName']['en-US'], icon_url=tiers['displayIcon'])
                skin_embed.set_thumbnail(url=skin_info['displayIcon'])
                skin_embed.set_image(url=png.line)
                new_embeds.append(skin_embed)
        button.label = new_label
        await interaction.response.edit_message(embeds=new_embeds, view=self)
