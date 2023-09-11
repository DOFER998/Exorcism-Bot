import discord
from discord.ext import commands
from discord.ext.commands import slash_command

from data.database import get_skins_lvl_uuid, get_content_tiers
from inter.buttons.skins_buttons import SwitchingBetweenStores
from utils.apis.in_game.get_store import get_store
from utils.user_check import check_user
from data.settings import png


class Store(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="store", description="Показывает ваш магазин повседневных товаров и аксессуаров")
    async def store(
            self,
            ctx: discord.ApplicationContext,
    ):
        await ctx.defer()

        user_riot_info = await check_user(user_id=str(ctx.user.id))
        store_info = get_store(
            access_token=user_riot_info['riot']['access_token'],
            entitlements_token=user_riot_info['riot']['entitlements_token'],
            region=user_riot_info['riot']['region'],
            puuid=user_riot_info['riot']['puuid']
        )

        embed_list = []

        embed = discord.Embed(title=" ",
                              description=f"Ежедневный магазин `{user_riot_info['riot']['player_name']}`\nОсталось времени до смены: {store_info[1]}",
                              color=0xf20057)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
        embed.set_image(url=png.line)
        embed_list.append(embed)
        for skin in store_info[0]:
            skin_info = await get_skins_lvl_uuid(skin['id'])
            tiers = await get_content_tiers(skin_info['contentTierUuid'])
            skin_embed = discord.Embed(title=" ",
                                       description=f"<:ValorantPointIcon:1137697062406856704> `{skin['cost']}`")
            skin_embed.set_author(name=skin_info['displayName']['en-US'], icon_url=tiers['displayIcon'])
            skin_embed.set_thumbnail(url=skin_info['displayIcon'])
            skin_embed.set_image(url=png.line)
            embed_list.append(skin_embed)
        await ctx.respond(embeds=embed_list, view=SwitchingBetweenStores())


def setup(bot):
    bot.add_cog(Store(bot))