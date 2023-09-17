import discord
from discord.ext import commands
from discord.ext.commands import slash_command

from inter.modals.questionnaire_modal import QuestionnaireModal


class Questionnaire(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="questionnaire", description="Отправьте свою анкету для того чтобы найти себе команду")
    @commands.guild_only()
    async def questionnaire(
            self,
            ctx: discord.ApplicationContext,
    ):
        modal = QuestionnaireModal(self.bot)
        await ctx.send_modal(modal)


def setup(bot):
    bot.add_cog(Questionnaire(bot))
