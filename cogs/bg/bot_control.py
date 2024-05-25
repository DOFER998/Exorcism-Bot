import asyncio
import discord
from discord.ext import commands

from data.database import add_users, leave_user


class BotControl(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if not member.bot:
            await add_users(user_id=member.id)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        if not member.bot:
            await leave_user(user_id=member.id)


def setup(bot):
    bot.add_cog(BotControl(bot))
