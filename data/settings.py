from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = 'mongodb://localhost:27017'
    token: str = 'token'
    guild_id: int = 123


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)


class PNG(BaseSettings):
    line: str = ('https://cdn.discordapp.com/attachments/1192538269565603891/1241313550601818133/line.png?ex=66505654'
                 '&is=664f04d4&hm=133340215efda1d3bcba10058996d35f176e7872947c4bfb9eb2928660f5c010&')
    titles: str = ('https://cdn.discordapp.com/attachments/1192538269565603891/1243133061810622464/title.webp?ex'
                   '=66505d62&is=664f0be2&hm=cb778856c030fd7f8d1874ddb6df6ef9d716734e9b685790043f870cf217015d&')


png = PNG()


class Color(BaseSettings):
    main_color: int = 0xd2a2ff


color = Color()


class Emoji(BaseSettings):
    v_point: str = '<:ValorantPointIcon:1243133869977505843>'
    k_credit: str = '<:KingdomCreditIcon:1243133871499907112>'
    expand: str = '<:expand:1241302642991566909>'
    shrink: str = '<:shrink:1241302646888075306>'


emoji = Emoji()

tiers_color = {
    '0cebb8be-46d7-c12a-d306-e9907bfc5a25': 0x009587,
    'e046854e-406c-37f4-6607-19a9ba8426fc': 0xf5955b,
    '60bca009-4182-7998-dee7-b8a2558dc369': 0xd1548d,
    '12683d76-48d7-84a3-4e09-6985794f0445': 0x5a9fe2,
    '411e4a55-4e59-7757-41f0-86a53f101bb5': 0xfad663,
}
