from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongodb_url: str = 'mongodb://localhost:27017'
    token: str = 'token'
    owner_id_0: int = 123
    owner_id_1: int = 123
    guild_id: int = 123
    error_channel_id: int = 123


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)


class PNG(BaseSettings):
    line: str = 'https://cdn.discordapp.com/attachments/1137752998525800538/1137835970457243648/1.png'
    titles: str = 'https://media.discordapp.net/attachments/1137752998525800538/1150975980958134332/ace-title_valorant_icon_50326.png?width=384&height=242'
    syntax: str = 'https://cdn.discordapp.com/attachments/1137752998525800538/1152196292538269706/syntax.png'
    bad: str = 'https://cdn.discordapp.com/attachments/1137752998525800538/1152196292924153966/bad.png'
    good: str = 'https://cdn.discordapp.com/attachments/1137752998525800538/1152196293272285225/good.png'
    excellent: str = 'https://cdn.discordapp.com/attachments/1137752998525800538/1152196293624594472/excellent.png'


png = PNG()


class Color(BaseSettings):
    main_color: int = 0xff4557


color = Color()


class Emoji(BaseSettings):
    v_point: str = '<:ValorantPointIcon:1137697062406856704>'
    k_credit: str = '<:KingdomCreditIcon:1137697058212556840>'
    expand: str = '<:expand:1177728090995175536>'
    shrink: str = '<:shrink:1177728147534401617>'
    yes: str = '<a:agree:1147230818163499009>'
    no: str = '<a:dontagree:1147230866083422259>'


emoji = Emoji()


class FeedbackChannelsId(BaseSettings):
    bug: int = 1137753032117977088
    feature: int = 1137753034772987944
    comment: int = 1137753037620916345


feedback = FeedbackChannelsId()


class TextChannelsIds(BaseSettings):
    questionnaire: int = 1137753089353465866
    approve_questionnaire: int = 1153066879812911275
    approve_logs_questionnaire: int = 1153648380933840987


text_channels = TextChannelsIds()

tiers_color = {
    '0cebb8be-46d7-c12a-d306-e9907bfc5a25': 0x009587,
    'e046854e-406c-37f4-6607-19a9ba8426fc': 0xf5955b,
    '60bca009-4182-7998-dee7-b8a2558dc369': 0xd1548d,
    '12683d76-48d7-84a3-4e09-6985794f0445': 0x5a9fe2,
    '411e4a55-4e59-7757-41f0-86a53f101bb5': 0xfad663,
}
