import discord
import datetime

from data.settings import color, png
from inter.buttons.admins_buttons import ApproveQuestionnaire


class QuestionnaireModal(discord.ui.Modal):
    def __init__(self, bot) -> None:
        super().__init__(title='Анкета')
        self.bot = bot
        self.add_item(
            discord.ui.InputText(
                label='Краткая информация о себе', style=discord.InputTextStyle.long, min_length=150, max_length=500))
        self.add_item(
            discord.ui.InputText(
                label='Кого ты ищешь', style=discord.InputTextStyle.long, min_length=150, max_length=500))
        self.add_item(
            discord.ui.InputText(
                label='Твой KD', style=discord.InputTextStyle.short, custom_id='kd'))
        self.add_item(
            discord.ui.InputText(
                label='Твой ранг', style=discord.InputTextStyle.short, custom_id='rang'))
        self.add_item(
            discord.ui.InputText(
                label='LVL Аккаунта Valorant', style=discord.InputTextStyle.short, custom_id='lvl'))

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            'Ваша анкета была принята на рассмотрение. Анкета будет рассмотрена в течении суток', ephemeral=True,
            delete_after=15)

        approve = discord.Embed(
            title='Новая анкета',
            description=f'**Краткая информация об игроке:**\n\n{self.children[0].value}\n\n\n**Кого ищет игрок:**\n\n{self.children[1].value}',
            color=color.main_color)
        approve.add_field(name='KD Игрока:', value=self.children[2].value, inline=True)
        approve.add_field(name='Ранг игрока:', value=self.children[3].value, inline=True)
        approve.add_field(name='LVL Аккаунта Valorant:', value=self.children[4].value, inline=True)
        approve.add_field(name='Прислал:', value=interaction.user.mention, inline=False)
        approve.set_footer(text=interaction.guild.name, icon_url=interaction.guild.icon.url)
        approve.set_thumbnail(url=interaction.user.display_avatar or interaction.user.default_avatar)
        approve.set_image(url=png.line)
        approve.timestamp = datetime.datetime.now()
        await self.bot.approve_questionnaire_channel.send(embed=approve, view=ApproveQuestionnaire(self.bot))
