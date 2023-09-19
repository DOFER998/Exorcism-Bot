import datetime

import discord

from data.settings import emoji, color


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
        logs = discord.Embed(title='Анкета подтверждена',
                             description=f'Была подтверждена анкета: [прыгнуть к анкете]({interaction.message.jump_url})',
                             color=color.main_color)
        logs.add_field(name='Ответственный за действие:', value=interaction.user.mention, inline=False)
        logs.set_thumbnail(url=interaction.user.display_avatar or interaction.user.default_avatar)
        logs.set_footer(text=interaction.guild.name, icon_url=interaction.guild.icon.url)
        logs.timestamp = datetime.datetime.now()
        await self.bot.approve_logs_questionnaire_channel.send(embed=logs)
        await self.bot.questionnaire_channel.create_thread(name='💭・Обсуждение', message=message)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(style=discord.ButtonStyle.red, emoji=discord.PartialEmoji.from_str(emoji.no), custom_id="no")
    async def no(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.yes.disabled = True
        self.no.disabled = True
        logs = discord.Embed(title='Анкета отклонена',
                             description=f'Была отклонена анкета: [прыгнуть к анкете]({interaction.message.jump_url})',
                             color=color.main_color)
        logs.add_field(name='Ответственный за действие:', value=interaction.user.mention, inline=False)
        logs.set_thumbnail(url=interaction.user.display_avatar or interaction.user.default_avatar)
        logs.set_footer(text=interaction.guild.name, icon_url=interaction.guild.icon.url)
        logs.timestamp = datetime.datetime.now()
        await self.bot.approve_logs_questionnaire_channel.send(embed=logs)
        await interaction.response.edit_message(view=self)
