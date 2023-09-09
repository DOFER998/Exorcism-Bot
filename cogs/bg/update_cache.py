import discord
from discord.ext import commands, tasks

from utils.content_cache import reload_cache


class UpdateCache(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.update_cache.start()

    def cog_unload(self) -> None:
        self.update_cache.cancel()

    @tasks.loop(hours=1)
    async def update_cache(self) -> None:
        await reload_cache()

    @update_cache.before_loop
    async def before_update_cache(self) -> None:
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(UpdateCache(bot))
