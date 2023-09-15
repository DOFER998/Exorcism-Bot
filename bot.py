import discord

from data.settings import settings

bot = discord.Bot(intents=discord.Intents.all(), owner_ids=[settings.owner_id_0, settings.owner_id_1],
                  debug_guild=settings.guild_id)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name='Valorant❤️'),
                              status=discord.Status.do_not_disturb)
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')


extensions = [
    # --------------------admin commands
    'cogs.admin.ping',
    # --------------------user commands
    'cogs.user.login',
    'cogs.user.store',
    'cogs.user.feedback',
    # --------------------system commands
    'cogs.bg.bot_control',
    'cogs.bg.update_cache',
    # --------------------error commands
    'cogs.error.error_handler',
]

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}: {e}')

bot.run(settings.token)
