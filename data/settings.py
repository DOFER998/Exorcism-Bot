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
