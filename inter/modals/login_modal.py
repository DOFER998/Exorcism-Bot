import discord
from datetime import datetime, timedelta

from data.database import login_user_in_riot
from utils.riot_auth.auth import Auth
from utils.riot_auth.auth_exceptions import RiotMultifactorError


class Modal2FALogin(discord.ui.Modal):
    def __init__(self, interaction: discord.Interaction, cookie: dict, message: str, label: str) -> None:
        super().__init__(title='Двухфакторная аутентификация', timeout=180.0)
        self.interaction: discord.Interaction = interaction
        self.cookie = cookie
        self.placeholder = message
        self.label = label

        self.add_item(
            discord.ui.InputText(label=self.label, placeholder=self.placeholder, min_length=6, max_length=6)
        )

    async def callback(self, interaction: discord.Interaction):
        code = self.children[0].value
        await interaction.response.defer(ephemeral=True)
        try:
            if code:
                auth = Auth()
                cookie = self.cookie

                authenticate = await auth.give2facode(code, cookie)

                if authenticate['auth'] == 'response':
                    auth_data = authenticate['data']
                    cookie = auth_data['cookie']['cookie']
                    access_token = auth_data['access_token']
                    token_id = auth_data['token_id']
                    entitlements_token = await auth.get_entitlements_token(access_token)
                    puuid, name, tag = await auth.get_userinfo(access_token)
                    region = await auth.get_region(access_token, token_id)
                    player_name = f'{name}#{tag}' if tag is not None and tag is not None else 'no_username'

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
                    await login_user_in_riot(user_id=interaction.user.id, data=data)

                    embed = discord.Embed(title='Успех!', description=f'Вы вошли в аккаунт `{player_name}`', color=0xf20057)
                    embed.set_footer(text=f'{interaction.guild.name} • Valorant', icon_url=interaction.guild.icon.url)
                    await interaction.followup.send(embed=embed, ephemeral=True, delete_after=5)
        except RiotMultifactorError as e:
            embed = discord.Embed(title='ОШИБКА!', description=f'{e}', color=0xf20057)
            embed.set_footer(text=f'{interaction.guild.name} • Valorant', icon_url=interaction.guild.icon.url)
            await interaction.followup.send(embed=embed, ephemeral=True, delete_after=10)
