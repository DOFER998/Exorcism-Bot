import discord
import datetime

from data.settings import color, png


class FeedbackModal(discord.ui.Modal):
    def __init__(self, placeholder, label, channel_id) -> None:
        super().__init__(title='Обратная связь')
        self.placeholder = placeholder
        self.label = label
        self.channel_id = channel_id
        self.add_item(
            discord.ui.InputText(label=self.label, placeholder=self.placeholder, style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        label = self.children[0].label
        value = self.children[0].value
        embed = discord.Embed(title='Благодарим вас за обратную связь ❤!', color=color.main_color)
        embed.set_footer(text=interaction.guild.name, icon_url=interaction.guild.icon.url)
        embed.set_image(url=png.line)
        await interaction.response.send_message(embed=embed, ephemeral=True, delete_after=10)

        embed_c = discord.Embed(
            title=label,
            description=f'`{value}`\n\n\nPS. {interaction.user.mention}',
            color=color.main_color)
        embed_c.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
        embed_c.set_footer(text=interaction.guild.name, icon_url=interaction.guild.icon.url)
        embed_c.set_image(url=png.line)
        embed_c.timestamp = datetime.datetime.now()
        await self.channel_id.send(embed=embed_c)
