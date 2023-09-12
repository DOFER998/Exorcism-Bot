import discord
from discord.ext import commands
from discord.commands import Option
from discord.ext.commands import slash_command

from data.settings import feedback
from inter.modals.feedback_modal import FeedbackModal


class Feedback(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='feedback', description='Оставьте свой отзыв')
    async def feedback(
            self,
            ctx: discord.ApplicationContext,
            type: Option(str, name='type', description='Укажите, какой тип отзыва вы хотите оставить',
                         choices=["Сообщить об ошибке", "Запросить функцию", "Оставить комментарий"])
    ):
        if type == 'Сообщить об ошибке':
            channel = self.bot.get_channel(feedback.bug)
            modal = FeedbackModal(
                placeholder='Расскажите мне больше об ошибке',
                label='Сообщить об ошибке',
                channel_id=channel
            )
        elif type == 'Запросить функцию':
            channel = self.bot.get_channel(feedback.feature)
            modal = FeedbackModal(
                placeholder='Какую функцию вы хотите создать?',
                label='Запросить функцию',
                channel_id=channel
            )
        else:
            channel = self.bot.get_channel(feedback.comment)
            modal = FeedbackModal(
                placeholder='Оставить комментарий о боте Ex0rcist#3795 или сервере Exorcism',
                label='Оставить комментарий',
                channel_id=channel)
        await ctx.send_modal(modal)


def setup(bot):
    bot.add_cog(Feedback(bot))
