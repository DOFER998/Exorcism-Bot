import discord
from discord.ext import commands
from discord.commands import Option
from discord.ext.commands import slash_command
from datetime import datetime, timedelta

from data.database import login_user_in_riot
from data.settings import color
from utils.riot_auth.auth import Auth
from utils.riot_auth.auth_exceptions import RiotRatelimitError, RiotAuthenticationError, RiotUnknownErrorTypeError
from inter.modals.login_modal import Modal2FALogin


class Login(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="login", description="Вход в систему с помощью учетной записи Riot")
    @commands.guild_only()
    async def login(
            self,
            ctx: discord.ApplicationContext,
            username: Option(input_type=str, description='Введите имя пользователя учетной записи Riot'),
            password: Option(input_type=str, description='Введите пароль учетной записи Riot')
    ):

        try:
            auth = Auth()
            authenticate = await auth.authenticate(username, password)
            if authenticate['auth'] == 'response':
                await ctx.defer(ephemeral=True)
                auth_data = authenticate['data']
                cookie = auth_data['cookie']['cookie']
                access_token = auth_data['access_token']
                token_id = auth_data['token_id']
                entitlements_token = await auth.get_entitlements_token(access_token)
                puuid, name, tag = await auth.get_userinfo(access_token)
                region = await auth.get_region(access_token, token_id)
                player_name = f'{name}#{tag}' if tag is not None and name is not None else 'no_username'

                expiry_token = datetime.timestamp(datetime.utcnow() + timedelta(minutes=59))
                data = dict(
                    puuid=puuid,
                    region=region,
                    access_token=access_token,
                    entitlements_token=entitlements_token,
                    token_id=token_id,
                    player_name=player_name,
                    cookie=cookie,
                    expiry_token=expiry_token
                )
                await login_user_in_riot(user_id=ctx.user.id, data=data)

                embed = discord.Embed(title='Успех!', description=f'Вы вошли в аккаунт `{player_name}`',
                                      color=color.main_color)
                embed.set_footer(text=f'{ctx.guild.name} • Valorant', icon_url=ctx.guild.icon.url)
                await ctx.respond(embed=embed, ephemeral=True, delete_after=5)
            elif authenticate['auth'] == '2fa':
                cookies = authenticate['cookie']
                message = authenticate['message']
                label = authenticate['label']
                modal = Modal2FALogin(ctx.interaction, cookies, message, label, self.bot)
                await ctx.send_modal(modal)
        except RiotAuthenticationError as e:
            embed = discord.Embed(title='ОШИБКА!', description=f'{e}', color=color.main_color)
            embed.set_footer(text=f'{ctx.guild.name} • Valorant', icon_url=ctx.guild.icon.url)
            await ctx.respond(embed=embed, ephemeral=True, delete_after=10)
        except RiotRatelimitError as e:
            embed = discord.Embed(title='ОШИБКА!', description=f'{e}', color=color.main_color)
            embed.set_footer(text=f'{ctx.guild.name} • Valorant', icon_url=ctx.guild.icon.url)
            await ctx.respond(embed=embed, ephemeral=True, delete_after=10)
        except RiotUnknownErrorTypeError as e:
            embed = discord.Embed(title='ОШИБКА!', description=f'{e}', color=color.main_color)
            embed.set_footer(text=f'{ctx.guild.name} • Valorant', icon_url=ctx.guild.icon.url)
            await ctx.respond(embed=embed, ephemeral=True, delete_after=10)


def setup(bot):
    bot.add_cog(Login(bot))
