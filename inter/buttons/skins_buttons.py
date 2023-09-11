import discord

from data.settings import png


class SwitchingBetweenStores(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(style=discord.ButtonStyle.green,
                       emoji=discord.PartialEmoji.from_str("<:expand:1122514948694757377>"), custom_id="expand_store")
    async def image(self, button: discord.ui.Button, interaction: discord.Interaction):
        new_embeds = []
        for embed in interaction.message.embeds:
            if (type(embed.image.url) == str and "nm" in embed.image.url.lower()) or (
                    type(embed.thumbnail.url) == str and "nm" in embed.thumbnail.url.lower()):
                new_embeds.append(embed)
                continue
            if 'expand' in button.emoji.name:
                new_emoji = discord.PartialEmoji.from_str("<:shrink:1122514947172216972>")
                if embed.thumbnail:
                    embed.set_image(url=embed.thumbnail.url)
                    embed.set_thumbnail(url=discord.Embed.Empty)
            elif 'shrink' in button.emoji.name:
                new_emoji = discord.PartialEmoji.from_str("<:expand:1122514948694757377>")
                if embed.image:
                    embed.set_thumbnail(url=embed.image.url)
                    embed.set_image(url=png.line)
            new_embeds.append(embed)
        button.emoji = new_emoji
        await interaction.response.edit_message(embeds=new_embeds, view=self)

    @discord.ui.button(style=discord.ButtonStyle.blurple, label='Магазин аксессуаров', custom_id='daily_shop')
    async def daily_shop(self, button: discord.ui.Button, interaction: discord.Interaction):
        ...
