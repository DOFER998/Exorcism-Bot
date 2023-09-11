import discord
from discord.ext import commands
from discord.commands import Option
from discord.ext.commands import slash_command


class Skin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='skin', description='Поиск скина для оружия VALORANT.')
    async def skin(
            self,
            ctx: discord.ApplicationContext,
            name: Option(input_type=str, description='Введите название скина(Исключительно на английском языке)')
    ):
        ...
