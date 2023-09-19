import discord
from discord.ext import commands

from data.settings import settings, text_channels


class Exorcist(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            activity=discord.Activity(
                type=discord.ActivityType.competing, name='Valorant❤️'
            ),
            status=discord.Status.do_not_disturb,
            intents=discord.Intents.all(),
            allowed_mentions=discord.AllowedMentions.all(),
            owner_ids=[settings.owner_id_0, settings.owner_id_1],
            debug_guild=settings.guild_id
        )

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    @property
    def error_channel(self):
        return self.get_guild(settings.guild_id).get_channel(settings.error_channel_id)

    @property
    def questionnaire_channel(self):
        return self.get_guild(settings.guild_id).get_channel(text_channels.questionnaire)

    @property
    def approve_questionnaire_channel(self):
        return self.get_guild(settings.guild_id).get_channel(text_channels.approve_questionnaire)

    @property
    def approve_logs_questionnaire_channel(self):
        return self.get_guild(settings.guild_id).get_channel(text_channels.approve_logs_questionnaire)

    async def shutdown(self):
        await self.close()

    def starter(self):
        extensions = [
            # --------------------admin commands
            'cogs.admin.ping',
            # --------------------user commands
            'cogs.user.login',
            'cogs.user.store',
            'cogs.user.feedback',
            'cogs.user.questionnaire',
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
