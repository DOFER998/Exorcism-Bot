import discord

from data.settings import emoji


class ApproveQuestionnaire(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(style=discord.ButtonStyle.green, emoji=discord.PartialEmoji.from_str(emoji.yes), custom_id="yes")
    async def yes(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.yes.disabled = True
        self.no.disabled = True
        new_embeds = []
        for embed in interaction.message.embeds:
            new_embeds.append(embed)
        message = await self.bot.questionnaire_channel.send(embeds=new_embeds)
        await self.bot.questionnaire_channel.create_thread(name='💭・Обсуждение', message=message)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(style=discord.ButtonStyle.red, emoji=discord.PartialEmoji.from_str(emoji.no), custom_id="no")
    async def no(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.yes.disabled = True
        self.no.disabled = True
        await interaction.response.edit_message(view=self)
