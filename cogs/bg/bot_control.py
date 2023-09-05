import discord
from discord.ext import commands

from data.database import add_users


class BotControl(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        ...

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        ...

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        ...

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        ...

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if member.bot:
            pass
        else:
            await add_users(user_id=member.id)


def setup(bot):
    bot.add_cog(BotControl(bot))
