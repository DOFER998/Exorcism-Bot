import discord
from discord.ext import commands
from discord.ext.commands import slash_command

from data.database import get_skins_lvl_uuid, get_content_tiers
from inter.buttons.skins_buttons import SwitchingBetweenStores
from utils.apis.in_game.get_store import GetStore
from utils.user_check import check_user
from data.settings import png, tiers_color, color, emoji


class Store(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="store", description="Показывает ваш магазин повседневных товаров и аксессуаров")
    async def store(
            self,
            ctx: discord.ApplicationContext,
    ):

        user_riot_info = await check_user(user_id=str(ctx.user.id))

        if user_riot_info is None:
            error = discord.Embed(title=" ",
                                  description="Вы не зарегистрированы в нашей системе! Напишите </login:1150791708892733542> чтобы зарегистрироваться!",
                                  color=color.main_color)
            await ctx.respond(embed=error, ephemeral=True, delete_after=5)
        else:
            get_store = GetStore(
                access_token=user_riot_info['riot']['access_token'],
                entitlements_token=user_riot_info['riot']['entitlements_token'],
                region=user_riot_info['riot']['region'],
                puuid=user_riot_info['riot']['puuid']
            )
            store_info = await get_store.get_daily_store()

            if store_info is None:
                err = discord.Embed(title='ОШИБКА!', description='Произошла известная для нас ошибка, мы работаем над '
                                                                 'ее устранением, а пока повторите команду '
                                                                 '</store:1150829112336846950>', color=color.main_color)
                err.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
                err.set_image(url=png.line)
                await ctx.respond(embed=err, ephemeral=True, delete_after=5)
            else:
                await ctx.defer()
                embed_list = []

                embed = discord.Embed(title=" ",
                                      description=f"Ежедневный магазин `{user_riot_info['riot']['player_name']}`\nОсталось времени до смены: {store_info[1]}",
                                      color=color.main_color)
                embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
                embed.set_image(url=png.line)
                embed_list.append(embed)
                for skin in store_info[0]:
                    skin_info = await get_skins_lvl_uuid(skin['id'])
                    tiers = await get_content_tiers(skin_info['contentTierUuid'])
                    skin_embed = discord.Embed(title=" ",
                                               description=f"{emoji.v_point} `{skin['cost']}`",
                                               color=tiers_color[skin_info['contentTierUuid']])
                    skin_embed.set_author(name=skin_info['displayName']['en-US'], icon_url=tiers['displayIcon'])
                    skin_embed.set_thumbnail(url=skin_info['levels'][0]['displayIcon'])
                    skin_embed.set_image(url=png.line)
                    embed_list.append(skin_embed)
                await ctx.respond(embeds=embed_list, view=SwitchingBetweenStores(interaction=ctx.interaction))


def setup(bot):
    bot.add_cog(Store(bot))
