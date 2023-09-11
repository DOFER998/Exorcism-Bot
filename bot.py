import discord

from data.settings import settings
from inter.buttons.skins_buttons import SwitchingBetweenStores

bot = discord.Bot(intents=discord.Intents.all(), owner_id=settings.owner_id, debug_guild=settings.guild_id)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name='Valorant❤️'),
                              status=discord.Status.do_not_disturb)
    bot.add_view(SwitchingBetweenStores())
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')


extensions = [
    # --------------------admin commands
    # --------------------user commands
    'cogs.user.login',
    'cogs.user.store',
    # --------------------system commands
    'cogs.bg.bot_control',
    'cogs.bg.update_cache',
]

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}: {e}')

bot.run(settings.token)
