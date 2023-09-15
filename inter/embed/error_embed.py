import discord

from data.settings import color, png


class ErrorEmbed(discord.Embed):
    def __init__(self, description: str, title: str = "Error", *args, **kwargs):
        super().__init__(title=title, description=description, color=color.main_color, *args, **kwargs)


def error_pass(user_id):
    return ErrorEmbed(description=f'Пользователь <@{user_id}> совершил ошибку в логине или пароле') \
        .set_image(url=png.line)


def error_2fa(user_id):
    return ErrorEmbed(description=f'Пользователь <@{user_id}> совершил ошибку в коде 2FA') \
        .set_image(url=png.line)


def error_rate_limit(user_id):
    return ErrorEmbed(description=f'Пользователь <@{user_id}> получил ограниечение от Riot') \
        .set_image(url=png.line)


def error_unknown_error_type(user_id):
    return ErrorEmbed(description=f'Пользователь <@{user_id}> получил неизвестную ошибку от Riot') \
        .set_image(url=png.line)
