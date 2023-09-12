from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongodb_url: str = 'mongodb://localhost:27017'
    token: str = 'token'
    owner_id: int = 123
    guild_id: int = 123


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)


class PNG(BaseSettings):
    line: str = 'https://cdn.discordapp.com/attachments/1137752998525800538/1137835970457243648/1.png'
    titles: str = 'https://media.discordapp.net/attachments/1137752998525800538/1150975980958134332/ace-title_valorant_icon_50326.png?width=384&height=242'


png = PNG()

tiers_color = {
    '0cebb8be-46d7-c12a-d306-e9907bfc5a25': 0x009587,
    'e046854e-406c-37f4-6607-19a9ba8426fc': 0xf5955b,
    '60bca009-4182-7998-dee7-b8a2558dc369': 0xd1548d,
    '12683d76-48d7-84a3-4e09-6985794f0445': 0x5a9fe2,
    '411e4a55-4e59-7757-41f0-86a53f101bb5': 0xfad663,
}
