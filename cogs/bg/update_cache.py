import discord
from discord.ext import commands, tasks

from utils.content_cache import reload_cache
from utils.apis.officer.http.version import version
from data.database import get_val_version, add_version_in_db


class UpdateCache(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.update_cache.start()

    def cog_unload(self) -> None:
        self.update_cache.cancel()

    @tasks.loop(hours=1)
    async def update_cache(self) -> None:
        val = await get_val_version()
        if version.version != val.version:
            await add_version_in_db(data=version)
            await reload_cache()

    @update_cache.before_loop
    async def before_update_cache(self) -> None:
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(UpdateCache(bot))
