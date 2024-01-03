from dataclasses import dataclass
from environs import Env
from tgbot.data.data import DataStorage


@dataclass
class TgBot:
    token: str
    name: str
    version: str
    parse_mode: str


@dataclass
class Config:
    bot: TgBot
    data: DataStorage
    admin: int


def load_config(path: str):
    env = Env()
    env.read_env(path)

    return Config(
        bot=TgBot(
            token=env.str('API_TOKEN'),
            name=env.str('BOT_NAME'),
            version=env.str('BOT_VERSION'),
            parse_mode=env.str('BOT_PARSE_MODE')
        ),
        data=DataStorage().load(),
        admin=env.int('ADMIN_ID')
    )
