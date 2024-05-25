import discord
from discord.ext import commands
from discord.ext.commands import slash_command

from data.settings import color


class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='ping', description='Обратная связь бота')
    async def ping(
            self,
            ctx: discord.ApplicationContext
    ):
        embed = discord.Embed(title='Pong! ' f'{self.bot.latency * 1000:.2f} ms', color=color.main_color)
        await ctx.respond(embed=embed, ephemeral=True, delete_after=10)


def setup(bot):
    bot.add_cog(Ping(bot))
