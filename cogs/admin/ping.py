import discord
from discord.ext import commands
from discord.ext.commands import slash_command

from data.settings import png


class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="ping", description="Пинг и состояние бота в реальном времени")
    @commands.is_owner()
    async def ping(
            self,
            ctx: discord.ApplicationContext,
    ):
        if self.bot.latency <= 0.100:
            color = 0x35ff03
            description = f'Отличный. `{self.bot.latency * 1000:.2f}` ms'
            url = png.excellent
        elif self.bot.latency <= 0.300:
            color = 0xff8503
            description = f'Хороший. `{self.bot.latency * 1000:.2f}` ms'
            url = png.good
        elif self.bot.latency <= 0.500:
            color = 0xff0303
            description = f'Низкий. `{self.bot.latency * 1000:.2f}` ms'
            url = png.bad
        else:
            color = 0xfbff03
            description = f'Очень плохой. `{self.bot.latency * 1000:.2f}` ms'
            url = png.syntax
        embed = discord.Embed(title='Пинг и состояние бота в реальном времени', description=description, color=color)
        embed.set_thumbnail(url=url)
        embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon.url)
        await ctx.defer(ephemeral=True)
        await ctx.respond(embed=embed, ephemeral=True, delete_after=10)


def setup(bot):
    bot.add_cog(Ping(bot))
