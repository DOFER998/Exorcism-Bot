import discord
from discord.ext import commands


class ErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        handled = False

        async def send_error(*args, **kwargs):
            await ctx.respond(*args, ephemeral=True, **kwargs)

        if (cog := ctx.cog):
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                handled = True
                return
        ignore = (commands.CommandNotFound)
        if isinstance(error, ignore):
            handled = True
            return
        if isinstance(error, commands.NotOwner):
            handled = True
            await send_error("Извините, только владелец бота и сообщества может использовать эту команду!",
                             delete_after=10)
        if isinstance(error, commands.NoPrivateMessage):
            handled = True
            await send_error("Вы не можете использовать эту команду в DM.", delete_after=10)


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
