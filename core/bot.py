import discord
from discord.ext import commands

from data.settings import settings


class Exorcist(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            activity=discord.Activity(
                type=discord.ActivityType.competing, name='Valorant❤️'
            ),
            status=discord.Status.do_not_disturb,
            intents=discord.Intents.all(),
            allowed_mentions=discord.AllowedMentions.all(),
            debug_guild=settings.guild_id
        )

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    async def shutdown(self):
        await self.close()

    def starter(self):
        extensions = [
            # --------------------admin commands
            'cogs.admin.ping',
            # --------------------user commands
            'cogs.user.login',
            'cogs.user.store',
            'cogs.user.nightmarket',
            # --------------------system commands
            'cogs.bg.bot_control',
            'cogs.bg.update_cache',
            # --------------------error commands
            'cogs.error.error_handler',
        ]
        for extension in extensions:
            try:
                self.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}: {e}')
        self.run(settings.token)
